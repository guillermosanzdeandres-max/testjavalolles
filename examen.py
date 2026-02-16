
preguntas = [
    {
        "pregunta": "1. ¿Qué selección ganó el Mundial de 2010?\n"
                    "a) Brasil\n"
                    "b) Alemania\n"
                    "c) España\n"
                    "d) Argentina\n",
        "correcta": "c"
    },
    {
        "pregunta": "2. ¿En qué club jugó la mayor parte de su carrera Lionel Messi?\n"
                    "a) Real Madrid\n"
                    "b) FC Barcelona\n"
                    "c) Manchester City\n"
                    "d) Juventus\n",
        "correcta": "b"
    },
    {
        "pregunta": "3. ¿Cuántos jugadores hay en un equipo en el campo?\n"
                    "a) 9\n"
                    "b) 10\n"
                    "c) 11\n"
                    "d) 12\n",
        "correcta": "c"
    },
    {
        "pregunta": "4. ¿Qué país organiza la Premier League?\n"
                    "a) España\n"
                    "b) Italia\n"
                    "c) Alemania\n"
                    "d) Inglaterra\n",
        "correcta": "d"
    },
    {
        "pregunta": "5. ¿Qué jugador es conocido como CR7?\n"
                    "a) Neymar\n"
                    "b) Cristiano Ronaldo\n"
                    "c) Mbappé\n"
                    "d) Benzema\n",
        "correcta": "b"
    },
    {
        "pregunta": "6. ¿Cada cuántos años se celebra el Mundial?\n"
                    "a) 2\n"
                    "b) 3\n"
                    "c) 4\n"
                    "d) 5\n",
        "correcta": "c"
    },
    {
        "pregunta": "7. ¿Qué equipo ha ganado más Champions League?\n"
                    "a) FC Barcelona\n"
                    "b) Bayern Munich\n"
                    "c) Real Madrid\n"
                    "d) Liverpool\n",
        "correcta": "c"
    },
    {
        "pregunta": "8. ¿Qué tarjeta implica expulsión directa?\n"
                    "a) Amarilla\n"
                    "b) Roja\n"
                    "c) Azul\n"
                    "d) Verde\n",
        "correcta": "b"
    },
    {
        "pregunta": "9. ¿Cuánto dura un partido oficial (sin prórroga)?\n"
                    "a) 80 minutos\n"
                    "b) 90 minutos\n"
                    "c) 100 minutos\n"
                    "d) 120 minutos\n",
        "correcta": "b"
    }
]

correctas = 0
incorrectas = 0
informe = "# ⚽ Informe del Examen de Fútbol\n\n"

for i, p in enumerate(preguntas):
    respuesta = input(p["pregunta"] + "Tu respuesta (a/b/c/d o Enter para dejar en blanco): ").lower()

    if respuesta == "":
        informe += f"❔ Pregunta {i+1}: En blanco\n\n"
    elif respuesta == p["correcta"]:
        correctas += 1
        informe += f"✅ Pregunta {i+1}: Correcta\n\n"
    else:
        incorrectas += 1
        informe += f"❌ Pregunta {i+1}: Incorrecta\n\n"

nota = (correctas - incorrectas) * (10 / 9)

if nota < 0:
    nota = 0

nota = round(nota, 2)  # 🔹 Nota redondead

print("\nTu nota final es:", nota)

def animacion_aprobado():
    for _ in range(3):
        print("⚽🎉 ¡GOOOOL! ¡HAS APROBADO! 🎉⚽")
        time.sleep(0.5)

if nota < 2:
    print("Muy insuficiente 😞 Necesitas entrenar más.")
elif 3 <= nota < 5:
    print("Insuficiente 😕 Puedes mejorar bastante.")
elif 5 <= nota < 6:
    print("Suficiente 🙂 Has aprobado por poco.")
    animacion_aprobado()
elif 6 <= nota < 7:
    print("Bien 👍 Buen partido.")
    animacion_aprobado()
elif 7 <= nota < 9:
    print("Notable 👏 Gran actuación.")
    animacion_aprobado()
elif 9 <= nota < 10:
    print("Sobresaliente 🌟 Partido espectacular.")
    animacion_aprobado()
elif nota == 10:
    print("Excelente 🏆 ¡Hat-trick perfecto!")
    animacion_aprobado()

# ==========================
# GENERAR INFORME MARKDOWN
# ==========================

informe += f"## 📝 Resumen\n\n"
informe += f"- Correctas: {correctas}\n"
informe += f"- Incorrectas: {incorrectas}\n"
informe += f"- Nota final: {nota}\n"

with open("informe.md", "w", encoding="utf-8") as archivo:
    archivo.write(informe)

print("\n📄 Se ha generado el archivo 'informe.md' con el informe del examen.")

