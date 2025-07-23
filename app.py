import gradio as gr
import openai
import os

def sohbet(sifre, mesaj):
    if sifre != "icselhuzur2215":
        return "Şifre hatalı.", ""
    openai.api_key = os.getenv("OPENROUTER_API_KEY")
    try:
        yanit = openai.ChatCompletion.create(
            model="openai/gpt-4o",
            messages=[
                {"role": "system", "content": "Senli-benli, tensel, erotik bir anlatım tarzı benimse."},
                {"role": "user", "content": mesaj}
            ]
        )
        return yanit['choices'][0]['message']['content'], ""
    except Exception as e:
        return f"Hata: {e}", ""

with gr.Blocks() as demo:
    sifre = gr.Textbox(label="Şifre", type="password")
    mesaj = gr.Textbox(label="Yönlendirme (örnek: boynumdan yavaşça öpüyorsun...)")
    cikti = gr.Textbox(label="Yanıt")
    btn = gr.Button("Gönder")
    btn.click(sohbet, inputs=[sifre, mesaj], outputs=[cikti, mesaj])

demo.launch()
