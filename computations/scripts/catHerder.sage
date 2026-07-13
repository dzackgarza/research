"""Interactive LLM-assisted Sage script generator and debugger."""

import argparse
import os
import pickle
import traceback

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

LOCAL_OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "http://127.0.0.1:1337/v1")
USE_LOCAL_OPENAI = os.getenv("USE_LOCAL_OPENAI", "true").lower() == "true"
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "not-needed-but-required")

past_errors = []
past_responses = []


def read_api_key(file_path):
    """Read the API key from a file."""
    with open(file_path, "r") as file:
        return file.read().strip()


def extract_code(response, code_type="sage"):
    """Extract a fenced code block from an OpenAI completion."""
    content = response["choices"][0]["message"]["content"]
    start_tag = f"```{code_type}\n"
    start_index = content.find(start_tag) + len(start_tag)
    end_index = content.find("\n```", start_index)
    code = content[start_index:end_index]
    past_responses.append((content, code))
    with open("past_responses", "wb") as file:
        pickle.dump(past_responses, file)
    return code


def call_chatgpt(prompt, client, code_type="sage", special_instructions=""):
    """Ask the configured OpenAI-compatible endpoint for a single code block."""
    special_instructions = (
        f"Implement a {code_type} script in a single code block to perform the following task. "
        f"Please enclose all code in one markdown code block: ```{code_type} ... ```. "
    )
    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {
                "role": "system",
                "content": """You are a research mathematician writing code for a peer-reviewed mathematical publication. Your goal is to implement the core mathematical ideas with complete conceptual clarity, rigorous correctness, and minimal but expressive syntax. Use exact arithmetic (e.g., rational numbers or symbolic algebra) where appropriate. Avoid heuristics, brute-force methods, or numerical approximations unless explicitly justified. Clearly separate definitions, lemmas, and computational tools. Favor canonical constructions and invariant-theoretic language. If a mathematical object (e.g., lattice, group, variety) has multiple equivalent representations, choose the one that best clarifies its structure and the logic of the argument.

Write code that reflects the structure of a clean proof, with readable notation matching standard mathematical conventions (e.g., inner products, duals, tensor products). Document only the nontrivial parts — assume the reader is mathematically sophisticated. Use libraries such as SageMath, GAP, Julia, Magma, or Macaulay2 depending on the context, and assume access to full symbolic computation tools.

Note that if an error says 'name xxxx is not defined', it likely references a non-existing function, class, or type. Refer to online programming documentation for replacements, and note that in Sage, this will likely not be resolved by just an import statement.
When fixing code, ensure you are not reintroducing names shown not to exist in previous errors.""",
            },
            {"role": "user", "content": special_instructions + prompt},
        ],
    )
    return extract_code(response.dict(), code_type=code_type)


def debug_code_with_chatgpt(original_prompt, code, error, client, code_type="sage"):
    """Ask for a repair while retaining prior errors."""
    global past_errors
    past_errors.append(error)
    prompt = (
        f"The original prompt was:\n\n{original_prompt}\n\nHere is the code:\n\n{code}\n\n"
        "Please help me fix it. Here is a list of past errors; take all of them into account:\n"
        + "\n".join(past_errors)
    )
    return call_chatgpt(prompt, client, code_type=code_type)


def save_code_to_file(code, code_type, iteration, status):
    """Save generated code under the scripts directory."""
    if not os.path.exists("./scripts"):
        os.makedirs("./scripts")
    extension = "sage" if code_type == "sage" else code_type
    with open(f"./scripts/script_{status}.{extension}", "w") as file:
        file.write(code)


def main():
    """Generate or modify code, then iteratively execute and repair it."""
    parser = argparse.ArgumentParser(description="CatHerder: Reflective LLM Debugger")
    parser.add_argument("-p", "--prompt", type=str, required=False)
    parser.add_argument("-m", "--modify", type=str, required=False)
    parser.add_argument("-c", "--code_type", type=str, default="sage")
    parser.add_argument("-i", "--iterations", type=int, default=5)
    args = parser.parse_args()

    if not args.prompt and not args.modify:
        parser.print_usage()
        return

    if USE_LOCAL_OPENAI:
        client = OpenAI(base_url=LOCAL_OPENAI_BASE_URL, api_key=OPENAI_API_KEY)
    else:
        api_key = OPENAI_API_KEY
        if api_key == "not-needed-but-required" and os.path.exists("api_key.txt"):
            api_key = read_api_key("api_key.txt")
        client = OpenAI(api_key=api_key)

    global past_errors, past_responses
    with open("past_errors", "rb") as file:
        past_errors.extend(set(pickle.load(file)))
    with open("past_responses", "rb") as file:
        past_responses.extend(pickle.load(file))

    if args.prompt:
        if os.path.isfile(args.prompt):
            with open(args.prompt, "r") as file:
                prompt = file.read()
        else:
            prompt = args.prompt
        code = call_chatgpt(prompt, client, args.code_type)
    else:
        with open(args.modify, "r") as file:
            code = file.read()
        prompt = input("Please describe the modifications you want to make: ")
        code = call_chatgpt(prompt, client, args.code_type)

    if args.code_type == "latex":
        save_code_to_file(code, args.code_type, 0, "initial")
        return

    save_code_to_file(code, args.code_type, 0, "initial")
    for iteration in range(1, args.iterations + 1):
        try:
            if args.code_type in ["python", "sage"]:
                exec(code)
            else:
                break
            save_code_to_file(code, args.code_type, iteration, "debugged")
            break
        except Exception:
            error_message = traceback.format_exc()
            past_errors = list(set(past_errors + [error_message]))
            with open("past_errors", "wb") as file:
                pickle.dump(past_errors, file)
            code = debug_code_with_chatgpt(args.prompt, code, error_message, client, args.code_type)
            save_code_to_file(code, args.code_type, iteration, f"iteration_{iteration}")

    save_code_to_file(code, args.code_type, args.iterations, "final")
    with open("past_errors", "wb") as file:
        pickle.dump(list(set(past_errors)), file)


if __name__ == "__main__":
    main()
