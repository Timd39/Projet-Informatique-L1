import yfinance as yf
import pandas as pd

#dictionnaire contennant les action 
mes_actions = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Nvidia": "NVDA",
    "Alphabet (Google)": "GOOGL",
    "Amazon": "AMZN",
    "Meta (Facebook)": "META",
    "Tesla": "TSLA",
    "Broadcom": "AVGO",
    "Netflix": "NFLX",
    "AMD": "AMD",
    "Intel": "INTC",
    
    "LVMH": "MC.PA",
    "L'Oréal": "OR.PA",
    "Hermès": "RMS.PA",
    "TotalEnergies": "TTE.PA",
    "Sanofi": "SAN.PA",
    "Airbus": "AIR.PA",
    "Schneider Electric": "SU.PA",
    "Air Liquide": "AI.PA",
    "BNP Paribas": "BNP.PA",
    "Vinci": "DG.PA",
    "AXA": "CS.PA",
    "Danone": "BN.PA",
    "ASML (Pays-Bas)": "ASML.AS",
    
    "Coca-Cola": "KO",
    "PepsiCo": "PEP",
    "McDonald's": "MCD",
    "Nike": "NKE",
    "Disney": "DIS",
    "Visa": "V",
    "Mastercard": "MA",
    "JPMorgan Chase": "JPM",
    "Walmart": "WMT",
    "Johnson & Johnson": "JNJ",
    "Pfizer": "PFE",
    "Procter & Gamble": "PG",
    "Ferrari": "RACE",
    "Sony": "SONY",
    "Toyota": "TM",
    
    "S&P 500 (Top 500 US)": "SPY",
    "Nasdaq 100 (Tech US)": "QQQ",
    "CAC 40 ETF (France)": "EWQ",
    "Or (Gold Trust)": "GLD",
    "Marché Mondial (MSCI World)": "URTH",
    
    "Bitcoin (USD)": "BTC-USD",
    "Ethereum (USD)": "ETH-USD",
    "Solana (USD)": "SOL-USD",
    "Binance Coin (USD)": "BNB-USD",
    "Ripple (USD)": "XRP-USD",
    "Cardano (USD)": "ADA-USD"
}


#Vérification de si l'action est dans le dictionnaire
def verfi_action(action_choisie) :
    if action_choisie in mes_actions:
        return True
    else :
        return False
    
#Récupération de l'historique d'une action en fonction de sa période (temps total) et de son intervalle (temps à laquelle il prend les bougies sur la période)
def recuperer_historique(action_choisie,periode,intervalle):
    try :
        action_choisie = mes_actions[action_choisie]
        action_choisie = yf.Ticker(action_choisie)
    
        historique = action_choisie.history(period =periode,interval =intervalle)
    
        return historique
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération de {action_choisie} pour une période de {periode} et un intervalle de {intervalle}")

    

#Récupération du prix actuel de l'action
def recuperer_prix_actuel(action_choisie):
    if verfi_action(action_choisie):
        try :
            action_choisie = mes_actions[action_choisie]
            action = yf.Ticker(action_choisie)

            # permet de recuperer historique de l'action prix le plus bas/haut a l'ouverture/fermeture
            donnee_action = action.history(period = "1m")

            #recupere le dernier prix d'une action 
            prix_actuel = donnee_action['Close'].iloc[-1]
        
            return float(prix_actuel)
        except Exception as e:
            raise ValueError(f"Erreur, impossible de récupérer le prix actuel pour {action_choisie}")
    else :
        return TypeError(f"La vérification de l'action a retournée : {verfi_action(action_choisie)}")
