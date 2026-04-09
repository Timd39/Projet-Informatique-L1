# Projet-Informatique-L1



## Data 

On a importé la bibliothèque yfinance pour avoir accès aux données boursières. on n'utilisera pas l'ensemble des actions du marché pour le moment : on a créé une bibliothèque (une liste prédéfinie) contenant une cinquantaine d'actions. Cette liste est évolutive et pourra être enrichie ultérieurement.

on a aussi intègre plusieurs fonctions :
* Récupérer le prix en direct d'une action.
* Consulter l'historique des prix d'un actif.
* Vérifier si un symbole boursier est bien présent dans notre bibliothèque prédéfinie.

### Utilisation de yfinance

Pour interagir avec l'API de Yahoo Finance, on utilisons la structure suivante :

* **Ticker** : C'est l'objet de base de `yfinance`. En lui passant le symbole d'une action (ex: "AAPL" pour Apple), il cible l'actif et se prépare à récupérer ses données financières.
* **Période (`period`)** : Paramètre qui définit la plage de temps totale sur laquelle on souhaite récupérer les données. Par exemple : `"1d"` (1 jour), `"1mo"` (1 mois), `"1y"` (1 an), ou `"max"` (tout l'historique disponible).
* **Intervalle (`interval`)** : Paramètre qui définit la fréquence (le pas de temps) entre chaque point de donnée. Par exemple : `"1m"` (1 minute), `"1h"` (1 heure), `"1d"` (1 jour).
* **Historique (`history()`)** : C'est la méthode appelée sur l'objet Ticker pour télécharger concrètement les données en fonction de la `period` et de l'`interval` définis. Elle retourne un tableau de données (DataFrame Pandas) contenant les informations essentielles : prix d'ouverture (*Open*), de fermeture (*Close*), le plus haut (*High*), le plus bas (*Low*) et le volume des transactions (*Volume*).


## website 
### Multi-pages

j'ai mit le site en multi-pages pour pouvoir navigé plus facilement . 
* **`app.py`** : C'est le point d'entrée principal de l'application. Il gère l'état de session (`session_state`) et le système de connexion/inscription.

* **Dossier `pages/`** : Streamlit génère automatiquement un menu de navigation latéral à partir des fichiers présents dans ce dossier.permet de séparer clairement les fonctionnalités :
  * `1_Dashboard_Marche.py` : Pour la vision globale du marché en temps réel.
  * `2_Trading_et_Portefeuille.py` : Pour la gestion du "Paper Trading" et le suivi du portefeuille fictif.
  * `3_Analyse_et_IA.py` : Pour les outils mathématiques, le machine learning et le backtesting.

### Interface Graphique et Thème

j'ai voulue faire une interface qui ressemble a celle des plateformes de trading (si vous voulez des changemant demander moi ). 
La configuration visuelle est gérée par le fichier `.streamlit/config.toml`. je l'ai mit en theme sombre pour que sa soit moins fatigant  


### Système d'Authentification et Gestion des Sessions

Pour simuler un portefeuille personnel, j'ai développé un système de connexion basique.
* **Base de données** : Les informations des utilisateurs (Nom, Prénom, Âge, Email, Mot de passe,solde) sont stockées et lues via la bibliothèque `pandas` dans un fichier `data/compte.csv`.
* **État de session (Session State)** : on  `st.session_state` pour mémoriser si l'utilisateur est connecté (`connect = True`) et pour gérer la navigation dynamique entre la page de connexion et le formulaire de création de compte (`page_actuelle`).

### Visualisation des Données (Plotly)
 
Contrairement aux graphiques basiques de Streamlit, Plotly permet de générer des figures interactives (zoom, survol pour voir les prix exacts des actions, déplacement). Le graphique actuel trace l'évolution du prix de fermeture (`Close`) sur les 6 derniers mois .

### Fonctionnement de Streamlit et Commandes Utilisées




#### 1. Configuration et Textes
* `st.set_page_config(...)` : C'est la première commande Streamlit du script. Elle permet de configurer la page web (titre de l'onglet, icône, et mode d'affichage comme `layout="wide"` pour utiliser toute la largeur de l'écran).
* `st.title("Texte")` et `st.subheader("Texte")` : Permettent de structurer l'affichage avec des titres principaux et des sous-titres.

#### 2. Interactions Utilisateur 
* `st.text_input("Label")` : Crée une zone de saisie de texte. L'option `type="password"` permet de masquer les caractères a utiliser pour les mots de passe.
* `st.number_input("Label")` : Crée une zone de saisie numérique.
* `st.button("Texte")` : Génère un bouton cliquable. renvoie un booléen (`True` au moment où l'utilisateur clique), on peut donct utiliser dans des actions conditionnelles (`if st.button(...):`). `type="primary"` permet de mettre le bouton en surbrillance avec la couleur principale de notre thème.

#### 3. Messages de Statut (Retours visuels)
Streamlit possede des alertes visuelles pour guider l'utilisateur :
* `st.success("Message")` : Affiche un bandeau vert (ex: confirmation de création de compte).
* `st.error("Message")` : Affiche un bandeau rouge (ex: identifiants incorrects).
* `st.info("Message")` : Affiche un bandeau bleu (ex: information sur l'âge minimum requis).

#### 4. Intégration de Graphiques
* `st.plotly_chart(fig)` : Demande à Streamlit d'afficher le graphique interactif Plotly que qu'on a généré dans la variable `fig`, tout en l'adaptant à la largeur du conteneur.

#### 5. Gestion de l'État (Session State) et Navigation
Comme Streamlit recharge le script à chaque interaction, les variables normales se réinitialisent à chaque clic. Pour garder des informations en mémoire, on utiliseras  :
* `st.session_state` : Se comporte comme un dictionnaire Python qui conserve ses valeurs d'un rechargement à l'autre. on peut  utiliser pour mémoriser si l'utilisateur est connecté (`st.session_state["connect"] = True`) et pour savoir quelle vue afficher (`st.session_state.page_actuelle = "connexion"`).
* `st.rerun()` : Force Streamlit à interrompre l'exécution en cours et à recharger le script immédiatement.A utiliser pour actualiser l'interface directement après une connexion réussie ou un changement de page.
