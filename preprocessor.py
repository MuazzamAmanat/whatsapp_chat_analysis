import pandas as pd
import re


def preprocess(data):
    pattern = (
        r'\d{1,2}/\d{1,2}/\d{2,4},\s*'
        r'\d{1,2}:\d{2}'
        r'(?::\d{2})?'
        r'(?:\s*[\u202f\xa0 ]?[AaPp][Mm])?'
        r'\s*-\s*'
    )

    messages = re.split(pattern, data)[1:]
    dates = [
    d.replace("\u202f", " ")
     .replace("\xa0", " ")
     .replace(" - ", "")
     .strip()
    for d in re.findall(pattern, data)
]
    df=pd.DataFrame({'user_message':messages,'message_date':dates})
    df["message_date"] = (
    df["message_date"]
    .str.replace("\u202f", " ", regex=False)
    .str.replace("\xa0", " ", regex=False)
    .str.strip())
    df["message_date"] = pd.to_datetime(
    df["message_date"],format="mixed",dayfirst=True,errors="raise")
    df.rename(columns= {'message_date':'date'},inplace=True)
    #sepereate users and  their messages

    users = []
    messages = []
    for message in df['user_message']:
        entry = re.split(r'([\w\W]+?):\s', message)
        if entry[1:]:
            users.append(entry[1])
            messages.append(entry[2])
        else:
            users.append('group_notification')
            messages.append(entry[0])
    df['users'] = users
    df['messages'] = messages

    df.drop(columns=['user_message'], inplace=True)
    df['only_date'] = df['date'].dt.date
    df['only_date'] = pd.to_datetime(df['only_date']).dt.strftime('%d-%b-%Y')
    df['year']=df['date'].dt.year
    df['month']=df['date'].dt.month_name()
    df['day']=df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour']=df['date'].dt.hour
    df['minute']=df['date'].dt.minute
    

    return df
