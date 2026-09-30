(() => {
  const siteRoot = new URL(document.body.dataset.siteRoot || "./", document.baseURI);

  for (const form of document.querySelectorAll("[data-tag-lookup]")) {
    const input = form.querySelector("input");
    input.addEventListener("input", () => input.setCustomValidity(""));
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const page = new URL(`tag/${input.value.toUpperCase()}.html`, siteRoot);
      const response = await fetch(page, { method: "HEAD" });
      if (response.ok) {
        location.assign(page);
        return;
      }
      input.setCustomValidity("No lattice has this tag.");
      input.reportValidity();
    });
  }

  for (const button of document.querySelectorAll("[data-copy]")) {
    const label = button.textContent;
    button.addEventListener("click", async () => {
      await navigator.clipboard.writeText(document.getElementById(button.dataset.copy).textContent);
      button.textContent = "Copied";
      setTimeout(() => {
        button.textContent = label;
      }, 1500);
    });
  }
})();
