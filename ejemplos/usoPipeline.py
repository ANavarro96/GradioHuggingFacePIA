from transformers import pipeline
import gradio as gr


def describir_imagen(imagen):
    if imagen is None:
        raise gr.Error("Sube una imagen para describirla.")

    modelo = pipeline(
        "image-text-to-text", model="Salesforce/blip-image-captioning-base"
    )
    resultado = modelo(
        imagen, text="Describe this picture", max_new_tokens=50
    )
    print(f"Este tipo de modelos devuelve un {type(resultado)}")
    return resultado


def preguntita(pregunta):
    if not pregunta or not pregunta.strip():
        raise gr.Error("Escribe una pregunta.")

    chatgpt = pipeline(
        "text-generation", model="HuggingFaceTB/SmolLM2-135M-Instruct"
    )
    mensajes = [{"role": "user", "content": pregunta}]
    resultado = chatgpt(mensajes, max_new_tokens=128, return_full_text=False)
    print(f"Este tipo de modelos devuelve un {type(resultado)}")
    return resultado


def analizar_sentimiento(texto):
    if not texto or not texto.strip():
        raise gr.Error("Escribe un texto para analizarlo.")

    clasificador = pipeline(
        "sentiment-analysis",
        model="lxyuan/distilbert-base-multilingual-cased-sentiments-student",
    )
    resultado = clasificador(texto, top_k=None, truncation=True)
    print(f"Este tipo de modelos devuelve un {type(resultado)}")
    return str(resultado)


with gr.Blocks() as ui:
    with gr.Tab("Imagen a Texto"):
        gr.Interface(
            fn=describir_imagen,
            inputs=gr.Image(type="pil", label="Imagen"),
            outputs=gr.Textbox(label="Descripción (en inglés)"),
        )
    with gr.Tab("Preguntar al GPTo"):
        gr.Interface(
            fn=preguntita,
            inputs=gr.Textbox(label="Pregunta"),
            outputs=gr.Textbox(label="Respuesta"),
        )
    with gr.Tab("Análisis de sentimientos"):
        gr.Interface(
            fn=analizar_sentimiento,
            inputs=gr.Textbox(label="Texto", placeholder="Me ha encantado este producto."),
            outputs=gr.Label(label="Sentimiento", num_top_classes=3),
            examples=[["Me ha encantado este producto."], ["No funciona y es muy malo."]],
        )


if __name__ == "__main__":
    ui.launch()

