from googletrans import Translator
import google.generativeai as palm

def translate_text(text, target_language='en'):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

def main():
    palm.configure(api_key='BARD_API_KEY')

    # Seleccionar el modelo que admite la generación de texto
    models = [m for m in palm.list_models() if 'generateText' in m.supported_generation_methods]
    if not models:
        print("No hay modelos disponibles para la generación de texto. Verifica tu configuración o inténtalo más tarde.")
        exit()

    model = models[0].name

    print("Bienvenido al generador de texto. Escribe 'exit' para salir.")
    while True:
        # Solicitar al usuario que ingrese una pregunta
        user_input = input("Pregunta: ")

        # Salir del bucle si el usuario escribe 'exit'
        if user_input.lower() == 'exit':
            print("Hasta luego. ¡Adiós!")
            break

        # Traducir la pregunta al inglés
        translated_input = translate_text(user_input, target_language='en')

        # Generar la respuesta usando el modelo
        completion = palm.generate_text(
            model=model,
            prompt=translated_input,
            temperature=0,
            max_output_tokens=800,
        )

        # Traducir la respuesta al español
        translated_output = translate_text(completion.result, target_language='es')

        # Mostrar la respuesta generada
        print("Respuesta:", translated_output)

if __name__ == "__main__":
    main()
