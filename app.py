import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard IA - Satisfaction Client")

st.write("Bienvenue dans le dashboard du projet SMC Insight.")

# Simulation de données
data = {
    "Sentiment": ["Positif", "Neutre", "Négatif"],
    "Nombre": [320, 150, 80]
}

df = pd.DataFrame(data)

# KPI
col1, col2, col3 = st.columns(3)

col1.metric("Messages analysés", "550")
col2.metric("Clients à risque", "42")
col3.metric("Score moyen satisfaction", "78%")

st.subheader("Répartition des sentiments")

st.bar_chart(df.set_index("Sentiment"))

# Sélecteur
sentiment = st.selectbox(
    "Choisir un sentiment",
    df["Sentiment"]
)

st.write("Sentiment sélectionné :", sentiment)
