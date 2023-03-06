import requests

url = "https://api.consumet.org/anime/enime/onepiece"
response = requests.get(url, params={"page": 3})
data1 = response.json()
NN


url = "https://api.consumet.org/anime/enime/info?id=cl6ogc3hf00blaclu0x8m5yww"
response = requests.get(url)
data2 = response.json()



url = "https://api.consumet.org/anime/enime/watch?"
response = requests.get(url, params={
  "episodeId": "cl6q7lxgv1145672rtggz2oaiar",
  "server": "gogocdn"
})
data3 = response.json()


print(data1)
#print(data2)
#print(data3['headers']['Referer'])