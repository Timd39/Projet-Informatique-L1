import streamlit as st
import yfinance as yf
import plotly.graph_objects as go # On importe plotly
from data.data import MARKET

st.title("Courbe des action")

# Récupération des données
action_choisie = st.text_input("Quelle action souhaitez-vous analyser ?", "AAPL") # On prend le Bitcoin par exemple
action_choisie = MARKET[action_choisie]
data = yf.download(action_choisie, period="6mo")

st.subheader(f"Évolution de {action_choisie}")

# Création d'un graphique interactif avec Plotly
fig = go.Figure()

# On ajoute la courbe du prix
fig.add_trace(go.Scatter(
    x=data.index, 
    y=data['Close'].squeeze(), # squeeze() évite certains bugs d'affichage
    mode='lines', 
    name='Prix de fermeture',
    line=dict(color='red')
))

# On met en forme le graphique
fig.update_layout(
    title="Historique des prix",
    xaxis_title="Date",
    yaxis_title="Prix (USD)",
    template="plotly_white" # Un fond blanc propre
)

# On demande à Streamlit d'afficher le graphique Plotly
st.plotly_chart(fig, use_container_width=True)
