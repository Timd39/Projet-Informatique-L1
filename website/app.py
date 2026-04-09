import streamlit as st
import yfinance as yf
import plotly.graph_objects as go # On importe plotly
import pandas as pd
from data.data import MARKET,verifier_action

st.set_page_config()

base_utilisateurs = pd.read_csv("data/compte.csv")
def connection():
    st.title("Connexion à la Plateforme")
    mail = st.text_input("Adresse e-mail")
    password = st.text_input("Mot de passe",type="password")
    
    if st.button('ce connecter.') :
        compte_trouver = base_utilisateurs[base_utilisateurs["email"]==mail]
        
        if compte_trouver.empty :
            st.error("Identifiants incorrects. Veuillez réessayer.")
              
        else : 
            vrai_mot_de_passe = compte_trouver.iloc[0]["mot_de_passe"]
            
            if vrai_mot_de_passe == password :
                st.session_state["connect"] = True
                st.rerun()    
            else :
                st.error("Identifiants incorrects. Veuillez réessayer.")
                
    if st.button('creé un compte') : 
        st.session_state.page_actuelle = "nouvelle_utilisateur"
        st.rerun()   
        
        
        
        
def cree_compte():
    prenom = st.text_input("quel est votre nom ?","Bruce")
    nom =st.text_input("quel est votre nom ?","Wayne")
    
    nouv_compte_mail = st.text_input("Adresse e-mail","Entrez votre adresse e-mail")
    nouv_compte_pass = st.text_input("Mot de passe","Saisissez votre mot de passe",type="password")
    
    
    base_utilisateurs["email"]= nouv_compte_mail
    base_utilisateurs["mot_de_passe"] = nouv_compte_pass
    base_utilisateurs["nom"] = nom
    base_utilisateurs["prenom"] = prenom




def affiche_graphique(action_choisie) :
    st.title("Courbe des action")
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




  
if "page_actuelle" not in st.session_state:
    st.session_state.page_actuelle = "connexion"
if "connect"not in st.session_state :
    st.session_state["connect"] = False

if st.session_state.page_actuelle == "connexion":      
    if st.session_state["connect"] == False :
        connection()
        
if st.session_state.page_actuelle == "nouvelle_utilisateur" :
    cree_compte()








if st.session_state["connect"] == True :
    action_choisie = st.text_input("Quelle action souhaitez-vous analyser ?", "Apple")
    if st.button('Afficher la courbe des actions.'): 
        if verifier_action(action_choisie) :
            affiche_graphique(action_choisie)
            
        else :
            st.info("Désolé, cette action n'est pas disponible dans notre sélection actuelle.")
            
