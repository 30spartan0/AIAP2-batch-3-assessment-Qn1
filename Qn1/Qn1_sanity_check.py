
import pandas as pd

filename = 'hdb-property-information.csv'
data_raw = pd.read_csv(filename)

#Provide basic information on the dataset involved
def data_info(raw):
    print(raw.head())
    print(raw.info())
    print(raw.describe())
    print(raw.shape)
    print(raw.columns)
    
data_info(data_raw)

#Simple function to inform which column has missing values

def column_info(df):
    for i in df.columns:
        if df[i].isnull().values.any():
            print("column " + i + " has missing values")
        else:
            print("there is no null data in column: " + i)
            

#Check again with another dataset and change some value to NaN to validate column info

filename2 = 'URA_data.csv'       
data_URA = pd.read_csv(filename2)

data_info(data_URA)

column_info(data_URA)