import requests


hesders = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",
           "referer" : "https://global.wildberries.ru/catalog/5007120/detail.aspx"}

art = "5007120"

url = "https://basket-01.wbbasket.ru/vol50/part5007/5007120/info/ru/card.json"
print(url)
    
response = requests.get(url, headers = hesders)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error! {response.status_code}")


