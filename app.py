import streamlit as st
import pandas as pd

st.title("Dashboard IA - Satisfaction Client")
st.write("Bienvenue dans le dashboard du projet SMC Insight.")

# -------------------------
# Données simulées
# -------------------------
df_sentiment = pd.DataFrame({
    "Sentiment": ["Positif", "Neutre", "Négatif"],
    "Nombre": [320, 150, 80]
})

df_clients = pd.DataFrame({
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
})

# -------------------------
# Sidebar filtres
# -------------------------
st.sidebar.header("Filtres")

sentiment_filtre = st.sidebar.selectbox(
    "Sentiment dominant",
    ["Tous"] + df_clients["Sentiment_Dominant"].unique().tolist()
)

seuil_churn = st.sidebar.slider(
    "Seuil minimal de churn",
    0.0, 1.0, 0.5, 0.01
)

# -------------------------
# Filtrage
# -------------------------
df_clients_filtre = df_clients[df_clients["Score_Churn"] >= seuil_churn]

if sentiment_filtre != "Tous":
    df_clients_filtre = df_clients_filtre[
        df_clients_filtre["Sentiment_Dominant"] == sentiment_filtre
    ]

# -------------------------
# KPI
# -------------------------
col1, col2, col3 = st.columns(3)
col1.metric("Messages analysés", "550")
col2.metric("Clients à risque", str(len(df_clients_filtre)))
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
if not df_clients_filtre.empty:
    st.bar_chart(df_clients_filtre.set_index("Client")["Score_Churn"])
else:
    st.warning("Aucun client ne correspond aux filtres.")

# -------------------------
# Tableau clients à risque
# -------------------------
st.subheader("Tableau des clients à risque")
st.dataframe(df_clients_filtre, use_container_width=True)
st.subheader("Simulation de prédiction IA")

message = st.text_input("Entrer un message client")

if message:
    import random

    score = round(random.uniform(0.3, 0.95), 2)

    if score > 0.8:
        st.error(f"⚠ Risque élevé de churn : {score}")
    elif score > 0.6:
        st.warning(f"⚠ Risque modéré de churn : {score}")
    else:
        st.success(f"Client stable : {score}")
st.subheader("Évolution du risque de churn")

import numpy as np
import pandas as pd

dates = pd.date_range(start="2024-01-01", periods=10)

churn_trend = pd.DataFrame({
    "Date": dates,
    "Score moyen churn": np.random.uniform(0.4, 0.9, 10)
})

st.line_chart(churn_trend.set_index("Date"))
