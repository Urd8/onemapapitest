import requests
import json
import pandas as pd


#Read the File
df = pd.read_excel("Trial Address Input.xlsx")
#Read the Postal Code u want 
postal = df["Postal Code 1"].tolist()
results = []
for postal_code in postal:
    url = f"https://developers.onemap.sg/commonapi/search?searchVal={postal_code}&returnGeom=Y&getAddrDetails=Y&XY=Y"
    response = requests.get(url)
    data = json.loads(response.text)
    if "results" in data and len(data["results"]) > 0:
        address = data["results"][0]["ADDRESS"]
        x = data["results"][0]["X"]
        y = data["results"][0]["Y"]
        results.append({"Postal Code": postal_code, "Address": address, "X": x, "Y": y})
    else:
        results.append({"Postal Code": postal_code, "Address": "No address found.", "X": "", "Y": ""})
df_results = pd.DataFrame(results)

df_results.to_excel("Output.xlsx")
print(df_results)