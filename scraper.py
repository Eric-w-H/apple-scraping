from bs4 import BeautifulSoup
import requests
import urllib.request
import pandas as pd

if __name__ == "__main__":
  url = "https://www.apple.com/iphone/compare/"
  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")

  devices_parent = soup.find(True, {'class': 'device-list'})
  
  devices = devices_parent.findAll(True, {'class':'device-item'})
  name_list = list()
  specs_list = list(list())
  for device in devices:
    name_list.append(device.find(True, {'class':'device-title'}).text)
    specs_list.append([child.text for child in device.findAll('li')])

  data = pd.DataFrame(specs_list, name_list)
  data.to_csv('data.csv',sep='|')