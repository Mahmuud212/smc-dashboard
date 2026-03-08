import streamlit as st
import pandas as pd
import numpy as np

st.title("Dashboard IA - Satisfaction Client")
st.write("Bienvenue dans le dashboard du projet SMC Insight.")

# -------------------------
# Données simulées
# -------------------------
sentiment_data = {
    "Sentiment": ["Positif", "Neutre", "Négatif"],
    "Nombre": [320, 150, 80]
}
df_sentiment = pd.DataFrame(sentiment_data)

clients_data = {
    "Client": ["C001", "C002", "C003", "C004", "C005"],
    "Score_Churn": [0.82, 0.67, 0.91, 0.45, 0.76],
    "Sentiment_Dominant": ["Négatif", "Neutre", "Négatif", "Positif", "Négatif"],
    "Action": [
        "Appel prioritaire",
        "Suivi standard",
        "Geste commercial",
        "Aucune action",
        "Enquête satisfaction"
    ]
}
df_clients = pd.DataFrame(clients_data)

# -------------------------
# KPI
# -------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Messages analysés", "550")
col2.metric("Clients à risque", "4")
col3.metric("Score moyen satisfaction", "78%")

# -------------------------
# Graphique sentiments
# -------------------------
st.subheader("Répartition des sentiments")
st.bar_chart(df_sentiment.set_index("Sentiment"))

# -------------------------
# Graphique churn
# -------------------------
st.subheader("Scores de churn par client")
st.bar_chart(df_clients.set_index("Client")["Score_Churn"])

# -------------------------
# Tableau clients à risque
# -------------------------
st.subheader("Tableau des clients à risque")
st.dataframe(df_clients)

# -------------------------
# Sélecteur
# -------------------------
sentiment = st.selectbox(
    "Choisir un sentiment",
    df_sentiment["Sentiment"]
)

st.write("Sentiment sélectionné :", sentiment)
