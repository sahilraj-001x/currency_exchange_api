import requests
response = requests.get("https://currencyapi.net/api/v1/rates?key=8rWT755nh2zzX4Je8p9gnSDYTcCh9YPV8RSx&base=USD")

start = input("Enter the country whose currency value you want to know : ")
if start =="India":
    print()

data = response.json()
rates = data["rates"]

print(rates["INR"])