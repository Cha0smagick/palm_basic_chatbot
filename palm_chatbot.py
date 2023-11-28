import google.generativeai as palm

palm.configure(api_key='YOUR_BARD_API_KEY')

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

    # Generar la respuesta usando el modelo
    completion = palm.generate_text(
        model=model,
        prompt=user_input,
        temperature=0,
        max_output_tokens=800,
    )

    # Mostrar la respuesta generada
    print("Respuesta:", completion.result)
