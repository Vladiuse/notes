import requests

BASE_URL = "http://37.1.208.252:81/domain_checker/domains/"
BEARER = "c0e811b688d3066457d453ea74fdfb29cf5ff7b5"
headers = {
        "Authorization": f"Bearer {BEARER}",
        "Accept": "application/json",
    }

for _ in range(30):
    res = requests.get(BASE_URL, headers=headers)
    print(res.status_code)