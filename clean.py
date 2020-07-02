import string

def sort_out(elem):
  elem = elem.lower()
  # Name
  if 'iphone' in elem:
    return 0
  # Color
  if 'black' in elem or 'gold' in elem or 'gray' in elem:
    return 1
  # Display
  if 'inch' in elem:
    return 2
  # Make
  if 'design' in elem:
    return 3
  # Water resistance
  if 'depth' in elem:
    return 4
  # Back camera
  if 'mp camera' in elem:
    return 5
  # Front camera
  if 'camera' in elem:
    return 6
  # biometrics
  if ' id ' in elem:
    return 7
  # chip
  if 'chip' in elem:
    return 8
  # battery length
  if 'battery' in elem:
    return 9
  # wireless charge
  if 'wireless' in elem:
    return 10
  # fast charge
  if 'fast' in elem: 
    return 11

phone_costs = {
  "iPhone 11 Pro":              {'64':999,  '256':1149, '512':1349},
  "iPhone 11 Pro Max":          {'64':1099, '256':1249, '512':1449},
  "iPhone 11":                  {'64':699,  '128':749,  '256':849},
  "iPhone SE (2nd generation)": {'64':399,  '128':449,  '256':549},
  "iPhone XR":                  {'64':599,  '128':649}
}

if __name__ == "__main__":
  data = list()
  with open('./data.csv','r',encoding='utf8') as datafile:
    data = datafile.readlines()

  data = [line.split('|') for line in data]
  
  labels = ['Name','Color','Display','Make','Water Resistance','Back Camera','Front Camera','Biometrics','Chip','Battery','Wireless Charge','Fast Charge','64','128','256','512']
  sorted_data = [['' for _ in range(len(labels))] ]
  sorted_data[0][:] = labels

  for line in range(1,len(data)):
    sorted_data.append(['' for _ in range(len(labels))])
    for text in data[line]:
      elem = ''.join([x if x in string.printable else ' ' for x in text]).strip()
      index = sort_out(elem)
      if elem.strip() == '':
        continue
      sorted_data[line][index] = elem.strip()
    
      for sto_idx in range(len(labels)-4,len(labels)):
        try:
          sorted_data[line][sto_idx] = str(phone_costs[sorted_data[line][0]][labels[sto_idx]])
        except:
          pass

  with open('./cleaned-data.csv', 'w') as datafile:
    for line in sorted_data:
      for index in range(0, len(line) - 1):
        datafile.write(line[index])
        datafile.write('|')
      datafile.write(line[-1])
      datafile.write('\n')

