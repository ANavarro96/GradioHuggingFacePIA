import gradio as gr

def procesar(nombre, numero):
    saludo = f"Hola, {nombre or 'anónimo'}!"
    duplicado = int(numero) * 2
    es_par = (int(numero) % 2 == 0)
    return saludo, duplicado, es_par

with gr.Blocks(title="Botones") as demo:
    gr.Markdown("Ejemplo de uso de Button (y algo con columnas y filas)")

    with gr.Column():
        nombre = gr.Textbox(label="Nombre")
        with gr.Row():
            numero = gr.Slider(0, 10, value=5, step=1, label="Número")
            btn = gr.Button("Procesar")
    with gr.Column():
        salida_texto = gr.Textbox(label="Saludo")
        salida_num = gr.Number(label="Número x2")
        salida_bool = gr.Checkbox(label="¿Es par?")

    btn.click(
        fn=procesar,
        inputs=[nombre, numero],
        outputs=[salida_texto, salida_num, salida_bool]
    )

demo.launch()
