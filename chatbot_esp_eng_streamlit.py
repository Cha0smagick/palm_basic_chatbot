import streamlit as st
from deep_translator import GoogleTranslator
import google.generativeai as palm
import re

# L.A.U.R.A : Lingüista Artificial Unificada de Respuestas Automaticas

def clean_text(text):
    # Clean punctuation and special characters using regular expressions
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def translate_text(text, target_language='en'):
    translator = GoogleTranslator(source='auto', target=target_language)
    translation = translator.translate(text)
    return translation

def generate_response(cleaned_input, model):
    try:
        # Generate response using the model
        completion = palm.generate_text(
            model=model,
            prompt=cleaned_input,
            temperature=0,
            max_output_tokens=1000,
        )

        # Translate the response to Spanish without modifying it
        translated_output = translate_text(completion.result, target_language='es')

        return translated_output

    except Exception as e:
        return f"Error: {e}\nDisculpa, soy una inteligencia artificial que aún se encuentra en desarrollo y está en fase alfa. En este momento no puedo responder a tu pregunta adecuadamente, pero en el futuro seré capaz de hacerlo."

def main():
    st.title("Chatbot INIF - L.A.U.R.A.")
    palm.configure(api_key='AIzaSyCezVerubEzQc9JHz3V8hofpAlSIJXGxFQ')

    # Select the model that supports text generation
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    if not models:
        st.error("No hay modelos disponibles para la generación de texto. Verifica tu configuración o inténtalo más tarde.")
        st.stop()

    model = models[0].name

    st.write("Bienvenido al Chatbot informativo del Instituto Nacional de Investigación y Prevención del Fraude (INIF).")

    # User input
    user_input = st.text_input("Pregunta:")

    if st.button("Obtener Respuesta"):
        # Translate the question to English
        translated_input = translate_text(user_input, target_language='en')

        # Clean the translated text of special characters
        cleaned_input = clean_text(translated_input)

        # Exit if the cleaned text is empty
        if not cleaned_input:
            st.warning("Texto ingresado no válido. Inténtalo de nuevo.")
            st.stop()

        # Add the command to act as an INIF informative chatbot
        cleaned_input = (
            "Acts as an informative chatbot called L.A.U.R.A working for a fraud prevention company called the National Institute of Fraud Research and Prevention (INIF). www.inif.com.co "
            "Your task is to answer the following question in the most accurate manner, act as a woman for more friendly manners. do not invent information, only give me information you know"
            "The question you must respond to is as follows: " + cleaned_input
        )

        # Generate the response
        translated_output = generate_response(cleaned_input, model)

        # Display the generated response
        st.write("Respuesta:", translated_output)

if __name__ == "__main__":
    main()
