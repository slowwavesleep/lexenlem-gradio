from typing import Dict, List, Union

import gradio as gr
from lexenlem.preprocessing.adhoc import AdHocLemmatizer

title = "Lexicon-enhanced lemmatization for Estonian"

with open("./article.md") as file:
    article: str = file.read()

with open("./description.txt") as file:
    description: str = file.read()

models: Dict[str, AdHocLemmatizer] = {
    "Lemmatize": AdHocLemmatizer(path="vb_stanza_no_compound_no_deriv.pt", use_stanza=True),
    "Lemmatize with special symbols": AdHocLemmatizer(
        path="vb_stanza_symbols.pt", use_stanza=True, allow_compound_separator=True, allow_derivation_sign=True
    )
}

examples: List[List[Union[str, bool]]] = []
with open("examples.tsv") as file:
    for line in file:
        ex, flag = line.split("\t")
        flag = bool(int(flag))
        examples.append(
            [ex, flag]
        )


def predict(text: str, output_special_symbols: bool) -> List[str]:
    if output_special_symbols:
        return models["Lemmatize with special symbols"](text)
    else:
        return models["Lemmatize"](text)


demo = gr.Interface(
    fn=predict,
    title=title,
    description=description,
    article=article,
    inputs=[
        gr.inputs.Textbox(lines=7, label="Input text in the box below", placeholder="Text to lemmatize"),
        gr.inputs.Checkbox(label="Output special symbols")
    ],
    outputs=[
        gr.outputs.Textbox()
    ],
    examples=examples,
    allow_screenshot=False,
    allow_flagging="never",
)

demo.launch(debug=False, enable_queue=True, cache_examples=True)
