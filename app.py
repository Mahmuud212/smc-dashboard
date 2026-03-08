import streamlit as st

st.title("Dashboard IA - Satisfaction Client")

st.write("Bienvenue dans le dashboard du projet SMC Insight.")

sentiment = st.selectbox(
    "Choisir un sentiment",
    ["Positif", "Neutre", "Négatif"]
)

st.write("Sentiment sélectionné :", sentiment)
