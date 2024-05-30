import requests
import json

url = "http://127.0.0.1:8000/generate"

array = ["Vuejs", "React js"]

for i in range(len(array)):
    current = array[i]

    file = open(f"{current}.html", 'w')

    data = {
        "tech": current
    }

    r = requests.post(url, json=data)
    
    file.write(r.json())
    file.close()
