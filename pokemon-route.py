import requests
import json

pokemon=input("Choose a Species:\n>")

burp0_url = "https://pokeapi.co:443/api/v2/pokemon/"+pokemon
burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i", "Connection": "close"}
r=requests.get(burp0_url, headers=burp0_headers)
data=json.loads(r.text)
id=data["id"]

burp0_url = "https://pokeapi.co:443/api/v2/pokemon/"+str(id)+"/encounters"
burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i"}
r=requests.get(burp0_url, headers=burp0_headers)
data=json.loads(r.text)

versions=[]
for i in range(len(data)):
    for j in range(len(data[i]["version_details"])):
        if data[i]["version_details"][j]["version"]["name"] not in versions:
            versions.append(data[i]["version_details"][j]["version"]["name"])

print("Versions Avaliable")
for i in versions: 
    print("[+]",i)
version=input("\nChoose Version:\n>")

print(pokemon,"is found on locations as follows, choose which one you want:")

for i in range(len(data)):
    url=data[i]["location_area"]["url"]
    burp0_url = url
    burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "none", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i"}
    r=requests.get(burp0_url, headers=burp0_headers)
    data2=json.loads(r.text)

    for j in range(len(data2["pokemon_encounters"])):
        if data2["pokemon_encounters"][j]["pokemon"]["name"] == pokemon:
            for k in range(len(data[i]["version_details"])):
                if data[i]["version_details"][k]["version"]["name"] == version:
                    print("[+]","("+data[i]["version_details"][k]["version"]["name"]+")",data2["name"],"chance:",str(data2["pokemon_encounters"][j]["version_details"][0]["encounter_details"][0]["chance"])+"%","["+data2["pokemon_encounters"][j]["version_details"][0]["encounter_details"][0]["method"]["name"]+"]")
