from urlextract import URLExtract
url_extractor=URLExtract()
import matplotlib.pyplot as plt
import pandas as pd
import emoji

def fetch_stats(selected_user,df):
    if selected_user != "Overall" :
        num_messages=df[df['users']==selected_user].shape[0]     
        df=df[df['users']==selected_user]
        media_files=df[df['messages']=='<Media omitted>\n'].shape[0]    
        
        words=[]
        urls=[]
        for i in df['messages']:
            words.extend((i.split()))
            urls.extend(url_extractor.find_urls(i))

        return num_messages,len(words),media_files,len(urls),

    if selected_user=="Overall" :
        num_messages= df.shape[0]
        media_files=df[df['messages']=='<Media omitted>\n'].shape[0]    

        words=[]
        urls=[]

        for i in df['messages']:
            words.extend((i.split()))
            urls.extend(url_extractor.find_urls(i))

        return num_messages,len(words),media_files,len(urls)

#fetch_active_users
def fetch_active_users(df):
        df = df[df['users'] != 'group_notification']

        active_users=df['users'].value_counts().head()

        percent =(df['users'].value_counts() / df.shape[0]) * 100
        percent = percent.reset_index()
        percent.columns = ["User", "Percentage"]
        return active_users,percent




# create a wordcloud

from wordcloud import WordCloud
def word_cloud_generator(selected_user, df):

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    df = df[
        (df['users'] != 'group_notification') &
        (df['messages'] != '<Media omitted>\n')
    ]

    # read stopwords
    with open('romanEng2.csv', 'r') as f:
        stop_words = set(f.read().splitlines())

    words = []

    for message in df['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)


    cleaned_text = " ".join(words)

    wc = WordCloud(
        width=300,
        height=300,
        min_font_size=8,
        background_color='white'
    )

    wc_generated = wc.generate(cleaned_text)

    return wc_generated






#select top20 most used words but make sure there wont be any stopwords
from collections import Counter

def freq_counter(selected_user,df):

    with open('romanEng2.csv', 'r') as f:
        stop_words = set(f.read().splitlines())

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    df = df[
        (df['users'] != 'group_notification') &
        (df['messages'] != '<Media omitted>\n')
    ]

    words = []

    for message in df['messages']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    words_count = Counter(words).most_common(20)


    words_df = pd.DataFrame(
        words_count,
        columns=["Word", "How Many Times Used"]
    )

    return words_df


# emojis
def emoji_check(selected_user, df):

    emojis = []

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    for message in df['messages']:
        for char in message:
            if emoji.is_emoji(char):
                emojis.append(char)

    return Counter(emojis).most_common(10)


def monthly_chat_report (selected_user, df):
    if selected_user != 'Overall':
        df=df[df["users"]== selected_user]
    df['month_num']=df['date'].dt.month
    timeline_df = (df.groupby(["year", "month_num", "month"])["messages"].count().reset_index())

    timeline_df = timeline_df.sort_values(["year", "month_num"])
    time=[]
    for i in range(timeline_df.shape[0]):
        time.append(timeline_df['month'][i] + "-" + str(timeline_df['year'][i]))
    timeline_df['time']=time
    return timeline_df


def daily_chat_report(selected_user, df):
    if selected_user != "Overall":
        df = df[df["users"] == selected_user]

    daily_df = (
        df.groupby("only_date")["messages"]
        .count()
        .reset_index()
    )

    # latest 30 days
    daily_df = (
        daily_df.sort_values("only_date", ascending=False)
        .head(30)
        .sort_values("only_date")
    )

    return daily_df




def most_active_day(selected_user, df):

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    day_df = (
        df.groupby('day_name')['messages']
        .count()
        .reset_index()
    )

    days = [
        "Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"
    ]

    day_df['day_name'] = pd.Categorical(
        day_df['day_name'],
        categories=days,
        ordered=True
    )

    day_df = day_df.sort_values('day_name')

    return day_df



def most_active_month(selected_user, df):

    if selected_user != "Overall":
        df = df[df['users'] == selected_user]

    month_df = (
        df.groupby('month')['messages']
        .count()
        .reset_index()
    )

    months = [
        "January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"
    ]

    month_df['month'] = pd.Categorical(
        month_df['month'],
        categories=months,
        ordered=True
    )

    month_df = month_df.sort_values('month')

    return month_df



def most_active_member(df):

    member_df = (
        df[df['users'] != 'group_notification']
        ['users']
        .value_counts()
        .reset_index()
    )

    member_df.columns = ['users', 'messages']

    return member_df