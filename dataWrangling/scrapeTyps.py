import os, csv, json
import pandas as pd 


alldata = []
for file in os.listdir('C:/Users/apers/partXpush_data/data'):
    if file.endswith('.json'):
        with open(os.path.join('C:/Users/apers/partXpush_data/data', file), 'r') as filedata:
            subject = json.load(filedata)

            ## get training data
            
            subjtypicality = []
            if 'typicality' in subject['results'] and subject['results']['typicality'] != []:
                print('TRIGGERED')
                subjtypicality = pd.DataFrame(
                    subject['results']['typicality'][1:],
                    columns = subject['results']['typicality'][0],
                )   
                subjtypicality['condition'] = subject['condition']
                subjtypicality['id'] = subject['id']
                subjtypicality['phase'] = 'typicality'
                

                subjData = pd.concat([
                    subjtypicality 
                ], ignore_index = True)

                alldata.append(subjData)

alldata = pd.concat(alldata, ignore_index = True) 
alldata.to_csv('typResults.csv', index = None)

