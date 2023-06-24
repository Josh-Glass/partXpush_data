import os, csv, json
import pandas as pd 


alldata = []
for file in os.listdir('C:/Users/apers/partXpush_data/data'):
    if file.endswith('.json'):
        with open(os.path.join('C:/Users/apers/partXpush_data/data', file), 'r') as filedata:
            subject = json.load(filedata)

            ## get training data
            subjDataTrain = pd.DataFrame(
                subject['results']['trainPhase'][1:],
                columns = subject['results']['trainPhase'][0],
            )
            subjDataTrain['condition'] = subject['condition']
            subjDataTrain['id'] = subject['id']
            subjDataTrain['phase'] = 'trainPhase'

            ## get test data
            subjDataSubTest = pd.DataFrame(
                subject['results']['subTestPhase'][1:],
                columns = subject['results']['subTestPhase'][0],
            )
            subjDataSubTest['condition'] = subject['condition']
            subjDataSubTest['id'] = subject['id']
            subjDataSubTest['phase'] = 'subTestPhase'

            subjDataTestPhase = pd.DataFrame(
                subject['results']['testPhase'][1:],
                columns = subject['results']['testPhase'][0],
            )   
            subjDataTestPhase['condition'] = subject['condition']
            subjDataTestPhase['id'] = subject['id']
            subjDataTestPhase['phase'] = 'testPhase'
            '''
            if 'typicality' in subject['results'] and subject['results']['typicality'] != []:
                print('TRIGGERED')
                subjtypicality = pd.DataFrame(
                    subject['results']['typicality'][1:],
                    columns = subject['results']['typicality'][0],
                )   
                subjtypicality['condition'] = subject['condition']
                subjtypicality['id'] = subject['id']
                subjtypicality['phase'] = 'typicality'
                '''

            subjData = pd.concat([
                subjDataTrain, subjDataSubTest, subjDataTestPhase, 
            ], ignore_index = True)

            alldata.append(subjData)

alldata = pd.concat(alldata, ignore_index = True) 
alldata.to_csv('results.csv', index = None)

