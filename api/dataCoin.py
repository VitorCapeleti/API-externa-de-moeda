import requests
def get_data_coin():
    
    url = "https://api.coingecko.com/api/v3/simple/price?vs_currencies=usd%2Ceur&ids=bitcoin%2Cethereum&names=Bitcoin%2CEthereum&symbols=btc%2Ceth&include_market_cap=false&include_24hr_vol=false&include_24hr_change=false&include_last_updated_at=false&precision=2"

    headers = {
        "accept": "application/json",
        "x-cg-demo-api-key": "CG-1K1wEDiDVK9qHLx3fxAbG46h"
    }

    response = requests.get(url, headers=headers)
    return response.json()
#print(get_data_coin())
