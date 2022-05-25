from typing import Dict, List

import gradio as gr
from lexenlem.preprocessing.adhoc import AdHocLemmatizer

models: Dict[str, AdHocLemmatizer] = {
    "Lemmatize": AdHocLemmatizer(path="vb_stanza_no_compound_no_deriv.pt", use_stanza=True),
    "Lemmatize with special symbols": AdHocLemmatizer(
        path="vb_stanza_symbols.pt", use_stanza=True, allow_compound_separator=True, allow_derivation_sign=True
    )
}


def predict(text: str, model_name: str) -> List[str]:
    if model_name not in models:
        raise RuntimeError("Unknown model")
    return models[model_name](text)


gradio_ui = gr.Interface(
    fn=predict,
    title="Lexicon-enhanced lemmatization for Estonian",
    description="The purpose of this demo is to demonstrate the results of"
                " Lexicon-Enhanced Neural Lemmatization for Estonian developed by TartuNLP research group."
                " The idea is to utilize the input of an external resource"
                " (a `lexicon` — Vabamorf morphological analyzer in this particular case)"
                " as an additional input to improve the results of a neural lemmatizer model. Said additional input"
                " is a concatenation of one or more lemma candidates provided by Vabamorf. Morphological features and"
                " the part of speech are provided by Stanza in this demo, although it's possible to use native Vabamorf"
                " features as well (the results, however, are going to be slightly worse).\n\n"
                " The lexicon-enhanced lemmatizer itself is based on an older version of Stanza. The models were"
                " trained on the Estonian Dependency Treebank version 2.7.\n\n"
                " Two variants of lemmatization are provided in the demo: regular lemmatization and lemmatization with"
                " special symbols, which are `=` and `_`, denoting morphological derivation and separating parts of"
                " compound words respectively. The latter was trained on the original data with Vabamorf set to output"
                " these special symbols, while the latter was trained with `=` and `_` removed from the data and"
                " vabamorf output."
                "<img src='https://raw.githubusercontent.com/slowwavesleep/lexicon-enhanced-lemmatization/master/img"
                "/StanfordNLP_Lemmatizer-Overall_Modified.jpg' width=340 height=361>",
    inputs=[
        gr.inputs.Textbox(lines=7, label="Input text in the box below", placeholder="Text to lemmatize"),
        gr.inputs.Radio(list(models.keys()), label="Lemmatization type")
    ],
    outputs=[
        gr.outputs.Textbox()
    ],
    examples=[
        [
            "Ekspositsioonid võiksid alata juba kunstihotellide fuajeedest.",
            "Lemmatize"
        ],
        [
            "Ekspositsioonid võiksid alata juba kunstihotellide fuajeedest.",
            "Lemmatize with special symbols"
        ],
        [
            "Kõik uuritavad võeti vastu TÜ üld- ja molekulaarpatoloogia instituudis inimesegeneetika uurimisrühmas.",
            "Lemmatize with special symbols"
        ],
        [
            "Peamiselt viimasele toetub ka järgnev artikkel.",
            "Lemmatize"
        ],
        [
            "Arutletakse selle üle, mida ülearuse rahaga peale hakata.",
            "Lemmatize"
        ],
        [
            "Väikesele poisile tuuakse apteegist söögiisu tõstmiseks kalamaksaõli.",
            "Lemmatize"
        ],
        [
            "Tulevased beebid olid justkui peegeldusena pilgu beebisinas ja veel mingi ähmane lubadus.",
            "Lemmatize"
        ],
    ],
    allow_screenshot=False,
    allow_flagging="never",
)


gradio_ui.launch(debug=False, enable_queue=True)
