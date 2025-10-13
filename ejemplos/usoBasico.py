import gradio as gr

def saludar(nombre, apellido):
    return "Como estás, " + nombre + " " +  apellido + " ?"

demo = gr.Interface(
    fn=saludar,
    inputs=["text", "text"],
    outputs=["text"],
)

demo.launch() # podéis poner share=True para compartir el gradio