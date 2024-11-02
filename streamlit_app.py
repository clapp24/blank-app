import streamlit as st

st.title("🎈 My new Streamlit app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


liste_personen = ["Paul", "Anna", "Dieter", "Karl", "Sabrina", "Wiebke"]
liste_obst = ["Apfel", "Birne", "Pflaume", "Banane", "Orange"]
liste_staedte = ["Berlin", "München", "Hamburg", "Köln", "Frankfurt", "Dortmund", "Leipzig"]

auswahl_person = st.selectbox("Bitte eine Person auswählen", liste_personen)
auswahl_obst = st.selectbox("Bitte eine Obstsorte auswählen", liste_obst)
auswahl_stadt = st.selectbox("Bitte eine Stadt auswählen", liste_staedte)


if auswahl_person in ["Paul", "Dieter", "Karl"]:
  geschlecht = "Er"
else:
  geschlecht = "Sie"

st.write(f"{auswahl_person} kommt aus {auswahl_stadt}. {geschlecht} isst gerne {auswahl_obst}.")
