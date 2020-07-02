import pandas as pd
from matplotlib import pyplot as plt

if __name__ == '__main__':
  data = pd.read_csv('./cleaned-data.csv',sep='|')
  # print(data.columns)
  data['Battery'] = data['Battery'].apply(lambda x: float(x.split(' ')[4]))
  
  data = data.sort_values('Battery',ascending=False)

  data.plot.bar('Name','Battery')

  data['Display'] = data['Display'].apply(lambda x: float(x.split('-')[0]))
  data.plot.bar('Name','Display')

  data['Make'] = data['Make'].astype('string').apply(lambda x: 'NA' if x is pd.NA else 'STEEL' if 'steel' in x else 'ALUMINUM' if 'aluminum' in x else 'NA').astype('category')
  
  data['Chip'] = data['Chip'].apply(lambda x: int(x.split('A')[1].split(' ')[0])-7)
  data.plot.bar('Name','Chip')


  data.plot('Name',['64','128','256','512'],'bar')

  data['Hour per Dollar (64)'] = data['Battery'] / data['64']
  data['Hour per Dollar (128)'] = data['Battery'] / data['128']
  data['Hour per Dollar (256)'] = data['Battery'] / data['256']
  data['Hour per Dollar (512)'] = data['Battery'] / data['512']
  data.plot.bar('Name',['Hour per Dollar (64)','Hour per Dollar (128)','Hour per Dollar (256)','Hour per Dollar (512)'])

  data['GB per Dollar (64)'] = 64 / data['64']
  data['GB per Dollar (128)'] = 128 / data['128']
  data['GB per Dollar (256)'] = 256 / data['256']
  data['GB per Dollar (512)'] = 512 / data['512']
  data.plot.bar('Name',['GB per Dollar (64)','GB per Dollar (128)','GB per Dollar (256)','GB per Dollar (512)'])
  