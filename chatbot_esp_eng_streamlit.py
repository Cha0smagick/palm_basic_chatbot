import streamlit as st
from googletrans import Translator
import google.generativeai as palm
import re

# L.A.U.R.A : Lingüista Artificial Unificada de Respuestas Automaticas

def clean_text(text):
    # Clean punctuation and special characters using regular expressions
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    st.title("INIF Chatbot - L.A.U.R.A")

    # Streamlit user input for question
    user_input = st.text_input("Ask a question:")

    # Translate the question to English
    translated_input = translate_text(user_input, target_language='en')

    try:
        # Clean the translated text from special characters
        cleaned_input = clean_text(translated_input)

        # Check if the cleaned text is empty
        if not cleaned_input:
            st.warning("Invalid input. Please try again.")
            st.stop()

        # Add a prompt to act as an informative chatbot for INIF
        cleaned_input = (
            "Acts as an informative chatbot called L.A.U.R.A working for a fraud prevention company called the National Institute of Fraud Research and Prevention (INIF). www.inif.com.co "
            "Your task is to answer the following question in the most accurate manner, act as a woman for more friendly manners. do not invent information, only give me information you know"
            "The question you must respond to is as follows: " + cleaned_input
        )

        # Streamlit placeholder for displaying the response
        response_placeholder = st.empty()

        if st.button("Get Answer"):
            # Generate the response using the model
            completion = palm.generate_text(
                model=model,
                prompt=cleaned_input,
                temperature=0,
                max_output_tokens=1000,
            )

            # Translate the response back to Spanish without modification
            translated_output = translate_text(completion.result, target_language='es')

            # Display the generated response
            response_placeholder.success("Answer: " + translated_output)

    except Exception as e:
        st.error(f"Error: {e}")
        st.warning("Sorry, I am still in development and in the alpha phase. I may not be able to answer your question accurately at the moment, but I will improve in the future.")

if __name__ == "__main__":
    main()
