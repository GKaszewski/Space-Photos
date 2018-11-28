import urllib.parse, requests, json, webbrowser, random

main_api = 'https://images-api.nasa.gov/search?'

keyword=input('Type a keword: ')
#print(keyword)
url = main_api + urllib.parse.urlencode({'q':keyword,'media_type':'image'})
json_data = requests.get(url).json()
rndPhoto = random.randint(0, len(json_data['collection']['items']));
picture_collection = json_data['collection']['items'][rndPhoto]['href']
picture_data = requests.get(picture_collection).json()
picture_url = picture_data[0]
#print(picture_url)
webbrowser.open_new_tab(picture_url)