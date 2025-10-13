import gradio as gr

def funcion(nombre):
    return f"¡Cómo estás , {nombre}?"

with gr.Blocks() as demo:
    gr.Markdown("Pulsa *Ejecutar* :)")
    with gr.Row(): # Englobamos dos componentes en este bloque.
        inp = gr.Textbox(placeholder="¿Cómo te llamas?", label="Entrada")
        out = gr.Textbox(label="Salida")
    btn = gr.Button("Ejecutar")
    btn.click(fn=funcion, inputs=inp, outputs=out)

demo.launch()