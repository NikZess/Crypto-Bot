# ПРИМЕРНЫЙ АЛГОРИТМ РАБОТЫ С ВАЛЮТАМИ ПОКАЗА КУРСОВ (+ еще должна быть настройка бирж и orm запросы)

exchange_currencies = {
    "usdt": {"btc": "BTCUSDT", "ton": "TONUSDT", "doge": "DOGEUSDT", "usdc": "USDCUSDT"},
    "rub": {"btc": "BTCRUB", "ton": "TONRUB", "doge": "DOGERUB", "usdc": "USDCRUB"}
}

user_currency = input("Введите валюту: \n1. USDT \n2. RUB\n").lower()

if user_currency in exchange_currencies:
    data = exchange_currencies[user_currency]
    print(data)
    
    user_input = input("Введите валюту: ").lower()
    
    if user_input in data:
        print(data.get(user_input, 0))
    else:
        print("Такой валюты нет")
        
else:
    print("Неверная валюта")