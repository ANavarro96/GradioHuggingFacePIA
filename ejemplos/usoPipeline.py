from transformers import pipeline
import gradio as gr

itt = pipeline("image-to-text")
chatgpt = pipeline("text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct")
def preguntita(pregunta):
    mensaje = [ {"role": "user", "content": pregunta}]
    return chatgpt(mensaje)



with gr.Blocks() as ui:
    with gr.Tab("Imagen a Texto"):
        gr.Interface(fn = itt, inputs = gr.Image(type="pil"), outputs = gr.Text())
    with gr.Tab("Preguntar al GPTo"):
        gr.Interface(fn = preguntita,inputs = gr.Text(), outputs = gr.Text())

ui.launch()

