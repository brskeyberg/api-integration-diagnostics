import requests

url = "https://api.github.com"

response = requests.get(url, timeout=10)

print("Status code:", response.status_code)
print("Content-Type:", response.headers.get("Content-Type"))
print("Response URL:", response.url)
