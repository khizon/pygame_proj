import requests
import sys

r = requests.get("https://coreyms.com")

print(r.status_code)

print("Hello World")

