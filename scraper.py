import requests

url = "https://books.toscrape.com/"
try:
    response = requests.get(url, timeout=10)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        print("Conection Succesful!")
        print(response.text[:500])

except requests.exception.Timeout:
    print("The request time out.")
except requests.exceptions.ConnectionError:
    print("Connection failed.")
except requests.exceptions.RequestException as e:
    print("An error occured:", e)
