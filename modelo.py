from flask import Flask, render_template, request
import google.generativeai as genai

genai.configure(api_key="AIzaSyBSUXegwhMAjxmyQIBETkb_82uxikL3OH0")  # Reemplaza con tu clave real

model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

def traducir_texto(texto, idioma_destino):
    if not texto or not idioma_destino:
        return "Por favor, ingrese el texto y seleccione un idioma de destino."
    
    prompt = f"Traduce el siguiente texto al {idioma_destino}:\n\n{texto}"
    try:
        respuesta = model.generate_content(prompt)
        return respuesta.text if respuesta.parts else "No se pudo generar la traducción."
    except Exception as e:
        return f"Ocurrió un error: {e}"

@app.route("/", methods=["GET", "POST"])
def index():
    traduccion = ""
    if request.method == "POST":
        texto = request.form.get("texto")
        idioma = request.form.get("idioma")
        traduccion = traducir_texto(texto, idioma)
    return render_template("index.html", traduccion=traduccion)

if __name__ == "__main__":
    app.run(debug=True)
