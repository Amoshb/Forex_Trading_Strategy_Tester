import MetaTrader5 as mt5
import pandas as pd
from credentials import ACCOUNT, PASSWORD, SERVER
from datetime import datetime


if not mt5.initialize():
    print("MT5 Initialization failed")
    quit()

if mt5.login(ACCOUNT, password=PASSWORD,  server=SERVER):
    print(f"Logged in successfully to {SERVER} with account {ACCOUNT}")
    print()

    symbols = [ symbol.name for symbol in mt5.symbols_get()]
    MAJOUR_SYMBOLS = ['EURUSD_cl', 'GBPUSD_cl', 'USDJPY_cl', 'USDCHF_cl', 'AUDUSD_cl', 'USDCAD_cl', 'NZDUSD_cl','XAUUSD_cl']
    TIME_FRAMES = [ mt5.TIMEFRAME_M1 , mt5.TIMEFRAME_M5, mt5.TIMEFRAME_M15, mt5.TIMEFRAME_M30, mt5.TIMEFRAME_H1, mt5.TIMEFRAME_H4]
    rates = mt5.copy_rates_from(MAJOUR_SYMBOLS[0], TIME_FRAMES[-2], datetime(2024, 4, 1), 500)
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print(df)
    
mt5.shutdown()