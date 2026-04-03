
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


#verifie si l'action est dans le dictionnaire d'action 
def verfi_action(action_choisie) :
    if action_choisie in mes_actions:
        return True
    else:
        return False
    
    
def recuperer_historique(action_choisie,periode,intervalle):
    
    action_choisie = mes_actions[action_choisie]
    action_choisie = yf.Ticker(action_choisie)
    
    historique = action_choisie.history(period =periode,interval =intervalle)
    
    return historique
    

def recuperer_prix_actuel(action_choisie):
    if verfi_action(action_choisie) :
        action_choisie = mes_actions[action_choisie]
        action = yf.Ticker(action_choisie)
        donnee_action = action.history(period = "1m") # permet de recuperer historique de l'action prix le plus bas/haut a l'ouverture/fermeture
        
        prix_actuel = donnee_action['Close'].iloc[-1] #recupere le dernier prix d'une action 
        
        return float(prix_actuel)
    else :
        return -1
