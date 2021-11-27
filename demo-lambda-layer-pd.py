import json
import pandas as pd

def lambda_handler(event, context):
    df = pd.read_csv('test.csv')
    print(df.head(3))
    print(df.shape)
    print(df.columns)
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }