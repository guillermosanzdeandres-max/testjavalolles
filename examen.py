import streamlit as st

# Lista de preguntas (9 en total)
preguntas = [
    {"texto": "¿Qué país ha ganado más Mundiales?", 
     "opciones": ["Brasil", "Alemania", "Italia", "Argentina"], 
     "correcta": "Brasil"},

    {"texto": "¿Cuántos jugadores hay en el campo por equipo?", 
     "opciones": ["9", "10", "11", "12"], 
     "correcta": "11"},

    {"texto": "¿Qué jugador es conocido como CR7?", 
     "opciones": ["Cristiano Ronaldo", "Messi", "Mbappé", "Benzema"], 
     "correcta": "Cristiano Ronaldo"},

    {"texto": "¿Qué competición juegan los mejores clubes de Europa?", 
     "opciones": ["Europa League", "Champions League", "Conference League"], 
     "correcta": "Champions League"},

    {"texto": "¿Qué país ganó el Mundial 2010?", 
     "opciones": ["España", "Brasil", "Alemania"], 
     "correcta": "España"},

    {"texto": "¿Cuánto dura un partido de fútbol?", 
     "opciones": ["80 minutos", "90 minutos", "100 minutos"], 
     "correcta": "90 minutos"},

    {"texto": "¿Qué tarjeta significa expulsión?", 
     "opciones": ["Amarilla", "Roja", "Azul"], 
     "correcta": "Roja"},

    {"texto": "¿Qué jugador argentino ganó el Mundial 2022?", 
     "opciones": ["Messi", "Di María", "Agüero"], 
     "correcta": "Messi"},

    {"texto": "¿En qué club jugó muchos años Messi?", 
     "opciones": ["Barcelona", "PSG", "Inter Miami"], 
     "correcta": "Barcelona"}
]

st.title("⚽ Examen de fútbol")
st.write("Responde las preguntas y pulsa entregar para ver tu nota.")

# Creamos dos pestañas
tab1, tab2 = st.tabs(["Examen", "Informe"])

with tab1:

    with st.form("formulario"):

        respuestas_usuario = []

        # Mostrar preguntas
        for pregunta in preguntas:
            st.subheader(pregunta["texto"])

            opciones = [""] + pregunta["opciones"]  # opción en blanco
            respuesta = st.radio("Selecciona una opción:", opciones, key=pregunta["texto"])

            respuestas_usuario.append(respuesta)

        enviar = st.form_submit_button("Entregar examen")

    if enviar:

        aciertos = 0
        errores = 0
        total = len(preguntas)

        # Corrección
        for i in range(total):

            if respuestas_usuario[i] == "":
                pass  # si está en blanco no suma

            elif respuestas_usuario[i] == preguntas[i]["correcta"]:
                aciertos += 1

            else:
                errores += 1

        puntuacion = aciertos - errores
        nota = (puntuacion / total) * 10

        # Redondear la nota
        nota = round(nota, 2)

        st.header(f"Nota final: {nota} / 10")

        # Feedback según la nota
        if nota < 2:
            st.error("Muy insuficiente 😬")
        elif nota < 5:
            st.warning("Insuficiente")
        elif nota < 6:
            st.info("Suficiente")
            st.snow()
        elif nota < 7:
            st.success("Bien 👍")
            st.balloons()
        elif nota < 9:
            st.success("Notable ⭐")
            st.balloons()
        elif nota < 10:
            st.success("Sobresaliente 🏆")
            st.balloons()
        else:
            st.success("Excelente 💯")
            st.balloons()

        # Guardamos datos para el informe
        st.session_state["respuestas"] = respuestas_usuario

with tab2:

    st.header("Informe del examen")

    if "respuestas" in st.session_state:

        respuestas = st.session_state["respuestas"]

        informe = "# Resultados\n\n"

        for i in range(len(preguntas)):

            informe += f"### Pregunta {i+1}\n"
            informe += f"**Pregunta:** {preguntas[i]['texto']}\n\n"
            informe += f"**Tu respuesta:** {respuestas[i]}\n\n"
            informe += f"**Respuesta correcta:** {preguntas[i]['correcta']}\n\n"

            if respuestas[i] == preguntas[i]["correcta"]:
                informe += "✅ Correcta\n\n"
            else:
                informe += "❌ Incorrecta\n\n"

        st.markdown(informe)

    else:
        st.write("Primero tienes que hacer el examen.")
