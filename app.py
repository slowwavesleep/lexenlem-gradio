import gradio as gr
from lexenlem.preprocessing.vabamorf import VabamorfAdHocProcessor

lemmatizer = VabamorfAdHocProcessor(path="et_edt_lemmatizer.pt")

gradio_ui = gr.Interface(
    fn=lemmatizer.lemmatize,
    title="Lemmatization",
    description="Enter a text to lemmatize",
    inputs=[
        gr.inputs.Textbox(lines=7, label="Paste a text here"),
    ],
    outputs=[
        gr.outputs.Textbox()
    ],
    examples=["""
    Andmebaasid võimaldavad endas hoida struktureeritud andmeid ja nendest on väga lihtne neid kätte saada rakenduste jaoks. Andmebaasid on tihti vajalikud erinevate veebirakenduste jaoks. MySQL on üks kahest andmebaasi mootorist mida meie pakume. Teiseks on PostgreSQL.
    """],
    enable_queue=True,
    allow_screenshot=False,
    allow_flagging="never",
)

gradio_ui.launch(debug=True)
