import requests
response = requests.get("https://currencyapi.net/api/v1/rates?key=8rWT755nh2zzX4Je8p9gnSDYTcCh9YPV8RSx&base=USD")
i=0
print("\nCountry listed are India,united arab emirates,afghanistan,armania,netherlands Press stop to exit")
data = response.json()
rates = data["rates"]
while i<5:
    i += 1
    start = input("\nEnter the country whose currency value you want to know : ").lower()
    if start =="india":
        print("Country set to", start)
        currency = float(input("Enter the USD :"))
        print(rates["INR"]*currency)
    elif start =="united arab emirates":
        print("Country set to", start)
        currency = float(input("Enter the USD :"))
        print(rates["AED"]*currency)
    elif start =="afghanistan":
        print("Country set to", start)
        currency = float(input("Enter the USD :"))
        print(rates["AFN"]*currency)
    elif start =="armania":
        print("Country set to", start)
        currency = float(input("Enter the USD :"))
        print(rates["AMD"]*currency)
    elif start =="netherlands":
        print(rates["ANG"]*currency)
    elif start=="stop":
        print("...THANK YOU...")
        break
    else:
        print("Error...type not found")
