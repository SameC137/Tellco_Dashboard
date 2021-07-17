import pandas as pd
import numpy as np

def getTop(df,column,number=10,desc=' '):
    # print(f"\n Top 10 {desc} by {column}")
    return df.sort_values(by=column, ascending=False).head(number)

def getBottom(df,column,number,desc=' '):
    # print(f"\n Bottom {number} {desc} by {column}")
    return df.sort_values(by=column, ascending=False).tail(number)
def getMostFrequent(df,column,number,desc=' '):
    # print(f"\n Most frequent {number} by {column}")
    return df.sort_values(by=column, ascending=False).value_counts().nlargest(number)


def change_type(df):
    df["Start"]=pd.to_datetime(df["Start"], format='%m/%d/%Y %H:%M', errors='coerce')
    df["End"]=pd.to_datetime(df["End"], format='%m/%d/%Y %H:%M', errors='coerce')

    df['Handset Manufacturer'] = df['Handset Manufacturer'].astype('str')
    df['Last Location Name'] = df['Last Location Name'].astype('str')
    df['Bearer Id'] = df['Bearer Id'].apply(lambda x: '{:.0f}'.format(x))
    df['Bearer Id'] = df['Bearer Id'].astype('str')

    df['MSISDN/Number'] = df['MSISDN/Number'].astype('str')

    df['IMSI'] = df['IMSI'].astype('str')

    df['IMEI'] = df['IMEI'].astype('str')
    return df
    
def form_combination_columns(df):
    df['Total Data (Bytes)'] = df['Total DL (Bytes)'] + df['Total UL (Bytes)']
    df['Social Media (Bytes)'] = df['Social Media DL (Bytes)'] + df['Social Media UL (Bytes)']
    df['Google (Bytes)'] = df['Google DL (Bytes)'] + df['Google UL (Bytes)']
    df['Email (Bytes)'] = df['Email DL (Bytes)'] + df['Email UL (Bytes)']
    df['Youtube (Bytes)'] = df['Youtube DL (Bytes)'] + df['Youtube UL (Bytes)']
    df['Netflix (Bytes)'] = df['Netflix DL (Bytes)'] + df['Netflix UL (Bytes)']
    df['Gaming (Bytes)'] = df['Gaming DL (Bytes)'] + df['Gaming UL (Bytes)']
    df['Other (Bytes)'] = df['Other DL (Bytes)'] + df['Other UL (Bytes)']
    return df


def remove_null_session_id_and_user(df):
    df = df[~np.isnan(df['Bearer Id']) ]
    df = df[~np.isnan(df['MSISDN/Number']) ]
    return df

def fill_na(df):
    df=df.fillna(df.mean(skipna=True).to_dict())
    return df


def reduce_df(df):
    df = df.drop('Nb of sec with 37500B < Vol UL', 1)
    df = df.drop('Nb of sec with 6250B < Vol UL < 37500B', 1)
    df = df.drop('Nb of sec with 125000B < Vol DL', 1)
    df = df.drop('Nb of sec with 31250B < Vol DL < 125000B', 1)
    df = df.drop('Nb of sec with 1250B < Vol UL < 6250B', 1)
    df = df.drop('Nb of sec with 6250B < Vol DL < 31250B', 1)
    df = df.drop('Nb of sec with 1250B < Vol UL < 6250B', 1)
    df = df.drop('HTTP UL', 1)
    df = df.drop('HTTP DL', 1)
    df=df.drop([
'Social Media DL (Bytes)' ,
        'Social Media UL (Bytes)',
        'Google DL (Bytes)' , 
        'Google UL (Bytes)' ,
        'Email DL (Bytes)' , 
        'Email UL (Bytes)',
        'Youtube DL (Bytes)' , 
        'Youtube UL (Bytes)',
        'Netflix DL (Bytes)' , 
        'Netflix UL (Bytes)' ,
        'Gaming DL (Bytes)' , 
        'Gaming UL (Bytes)',
        'Other DL (Bytes)' , 
        'Other UL (Bytes)' ,
        'Total DL (Bytes)' , 
        'Total UL (Bytes)' ], axis = 1)
    return df


