/**
 * Sage-construct highlighting driven by the tree-sitter-sage grammar.
 *
 * The base Python layer stays with CodeMirror's maintained Lezer grammar;
 * this overlay recognizes exactly the Sage language delta with the same
 * grammar that drives the preamble's compiler, so Sage recognition has one
 * source of truth.
 */
import { Extension } from "@codemirror/state";
/**
 * CodeMirror extension highlighting Sage constructs via tree-sitter-sage.
 */
export declare function sageOverlay(): Extension;
