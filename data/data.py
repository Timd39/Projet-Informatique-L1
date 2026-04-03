import yfinance as yf
import pandas as pd

PERIODES_VALIDES = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
INTERVALLES_VALIDES = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]


#dictionnaire contennant les action 
MARKET = {
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
def verifier_action(action_choisie)->bool :
    return action_choisie in MARKET
    
#Récupération de l'historique d'une action en fonction de sa période (temps total) et de son intervalle (temps à laquelle il prend les bougies sur la période)
def recuperer_historique(action_choisie,periode : str,intervalle : str)-> pd.Dataframe:
    if not verifier_action(action_choisie):
        raise ValueError(f"'{action_choisie}' n'est pas dans le dictionnaire.")
    
    if periode not in PERIODES_VALIDES:
        raise ValueError(f"Période invalide : '{periode}'. Valeurs acceptées : {PERIODES_VALIDES}")
    
    if intervalle not in INTERVALLES_VALIDES:
        raise ValueError(f"Intervalle invalide : '{intervalle}'. Valeurs acceptées : {INTERVALLES_VALIDES}")
    try :

        ticker = MARKET[action_choisie]
        action = yf.Ticker(ticker)
        historique = action_choisie.history(period =periode,interval =intervalle)
    
        return historique
    
    except Exception as e:
        raise ValueError(f"Erreur lors de la récupération de {action_choisie} pour une période de {periode} et un intervalle de {intervalle}")

    

#Récupération du prix actuel de l'action
def recuperer_prix_actuel(action_choisie,periode : str)->float:
    if not verifier_action(action_choisie):
        raise ValueError(f"{action_choisie}n'est pas dans le dictionnaire")
    if periode not in PERIODES_VALIDES:
        raise ValueError(f"Période invalide : {periode}.")
    try :
        ticker = MARKET[action_choisie]
        action = yf.Ticker(ticker)

        # permet de recuperer historique de l'action prix le plus bas/haut a l'ouverture/fermeture
        donnee_action = action.history(period = periode)

        #recupere le dernier prix d'une action 
        prix_actuel = donnee_action['Close'].iloc[-1]
        
        return float(prix_actuel)
    
    except Exception as e:
        raise ValueError(f"Erreur, impossible de récupérer le prix actuel pour {action_choisie}")
