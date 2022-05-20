import gradio as gr
from lexenlem.preprocessing.adhoc import AdHocLemmatizer

lemmatizer = AdHocLemmatizer(path="vb_stanza_no_compound_no_deriv.pt", use_stanza=True)

gradio_ui = gr.Interface(
    fn=lemmatizer.__call__,
    title="Lemmatization",
    description="Enter a text to lemmatize",
    inputs=[
        gr.inputs.Textbox(lines=7, label="Enter or paste a text here"),
    ],
    outputs=[
        gr.outputs.Textbox()
    ],
    examples=["""Andmebaasid võimaldavad endas hoida struktureeritud andmeid ja nendest on väga lihtne neid kätte saada rakenduste jaoks.
    """],
    allow_screenshot=False,
    allow_flagging="never",
)

gradio_ui.launch(debug=True, enable_queue=True)
