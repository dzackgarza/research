import { EditorView, ViewUpdate, DecorationSet, WidgetType } from '@codemirror/view';
import { Extension } from '@codemirror/state';
import type { ILatexTypesetter } from '@jupyterlab/rendermime';
export declare class MathWidget extends WidgetType {
    readonly latex: string;
    readonly displayMode: boolean;
    readonly typesetter?: (ILatexTypesetter | null) | undefined;
    constructor(latex: string, displayMode: boolean, typesetter?: (ILatexTypesetter | null) | undefined);
    eq(other: MathWidget): boolean;
    toDOM(): HTMLElement;
    ignoreEvent(event: Event): boolean;
}
export declare class InlineCodeWidget extends WidgetType {
    readonly code: string;
    constructor(code: string);
    eq(other: InlineCodeWidget): boolean;
    toDOM(): HTMLElement;
    ignoreEvent(event: Event): boolean;
}
export declare class DocstringPreviewPluginClass {
    readonly view: EditorView;
    readonly typesetter?: (ILatexTypesetter | null) | undefined;
    decorations: DecorationSet;
    constructor(view: EditorView, typesetter?: (ILatexTypesetter | null) | undefined);
    update(update: ViewUpdate): void;
    buildDecorations(view: EditorView): DecorationSet;
}
export declare function createDocstringPreviewExtension(typesetter?: ILatexTypesetter | null): Extension;
