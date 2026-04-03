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
