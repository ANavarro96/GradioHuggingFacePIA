import gradio as gr

def saludar(nombre, pulsado, nota):
    saludo = "Hola " + nombre + " has sacado un " + str(nota)
    if pulsado:
        saludo += " pero eres repetidor!"
    return saludo, (nota > 5) # separar las salidas por coma

demo = gr.Interface(
    fn=saludar,
    inputs=["text", gr.Checkbox(label="Es repetidor"), gr.Slider(0, 100)],
    outputs=["text", gr.Checkbox(label="Aprobado")],
    # Cada una de la salidas de la función se relaciona con un componente
)
demo.launch()
