import streamlit as st
import pandas as pd 
import preprocessor, helper
import matplotlib.pyplot as plt
import emoji
import plotly.express as px


st.set_page_config(layout="wide")
# st.set_page_config(layout="centered")
st.sidebar.title("Whatsapp Chat Analysis")

uploaded_file=st.sidebar.file_uploader("Choose a Whatsapp_chat_file")

if uploaded_file is not None:

    if uploaded_file.name.endswith(".txt"):
        bytes_data = uploaded_file.getvalue()
        data = bytes_data.decode('utf-8')

        try:
            df = preprocessor.preprocess(data)
        except Exception:
            st.error("Unable to read this chat. Please make sure you upload the original WhatsApp chat exported **without media**.")
            st.stop()

    else:
        st.error("Please upload only a WhatsApp exported .txt file")
        st.stop()

    unique_users_list=df['users'].unique().tolist()
    unique_users_list.remove('group_notification')
    unique_users_list.sort()
    unique_users_list.insert(0,"Overall")
    selected_user = st.sidebar.selectbox("check data wrt individuals",unique_users_list)



if st.sidebar.button("Analyze Chat"):


    st.title("Overall Stats")
    num_messages,words,media_files,urls= helper.fetch_stats(selected_user,df) 
    col1,col2,col3,col4 = st.columns(4)
    with col1:
        st.subheader("Total Messages")
        st.title(num_messages)
    with col2:
        st.subheader("Total Words")
        st.title(words)
    with col3:
        st.subheader("Media Files")
        st.title(media_files)
    with col4:
        st.subheader("Links Shared")
        st.title(urls)
    st.title("")



    st.title("Most Active")

    day_df = helper.most_active_day(df)
    month_df = helper.most_active_month(df)
    member_df = helper.most_active_member(df)


    # Day and Month side by side
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Most Active Days")

        fig, ax = plt.subplots()
        ax.bar(day_df['day_name'], day_df['messages'], color='red')
        plt.xticks(rotation=45)

        st.pyplot(fig)


    with col2:
        st.subheader("Most Active Months")

        fig, ax = plt.subplots()
        ax.bar(month_df['month'], month_df['messages'], color='yellow')
        plt.xticks(rotation=45)

        st.pyplot(fig)


    # Member chart below
    st.subheader("Most Active Members")

    fig, ax = plt.subplots(figsize=(10,4))

    ax.bar(
        member_df['users'].head(10),
        member_df['messages'].head(10),
        color='green'
    )

    plt.xticks(rotation=45)

    st.pyplot(fig)






    st.title('Monthly Chat Report')
    monthly_chat_df=helper.monthly_chat_report(selected_user,df)
    fig,ax=plt.subplots(figsize=(10,5))
    ax.plot(monthly_chat_df['time'],monthly_chat_df['messages'])
    plt.xticks(rotation=60)
    st.pyplot(fig)


    st.title('Daily Chat Report')
    daily_chat_df = helper.daily_chat_report(selected_user, df)
    fig, ax = plt.subplots(figsize=(12,4))
    ax.plot(daily_chat_df['only_date'],daily_chat_df['messages'])
    plt.xticks(rotation=45)
    st.pyplot(fig)




    
    if selected_user == "Overall":
        active_user,percent=helper.fetch_active_users(df)
        names=active_user.index
        values=active_user.values
        fig, ax = plt.subplots(figsize=(11,7))
        col1,col2 =  st.columns(2)
        with col1:
            st.header("Most Active User")
            ax.bar(names,values,color='red')
            plt.xticks(rotation="vertical",fontsize=15)
            st.pyplot(fig)
        with col2:
            st.header("Active Time %")
            st.table(percent.style.format({"Percentage": "{:.2f}%"}))




    col1, col2= st.columns([1, 3])  
    with col2: 
        st.title("Mostly Used Word's Cloud")
        wc_img=helper.word_cloud_generator(selected_user,df)
        st.image(wc_img.to_array(),width=700)
        words_df=helper.freq_counter(selected_user,df)

    st.title("Most Used Words")
    st.dataframe(words_df)
    fig, ax = plt.subplots(figsize=(11,7))
    ax.bar(words_df["Word"],words_df["How Many Times Used"])
    ax.set_xlabel("Words")
    ax.set_ylabel("Frequency")
    ax.set_title("Most Used Words")
    plt.xticks(rotation=45)
    st.pyplot(fig)





    st.title("Top 10 emojis Used In Chat")
    emoji_df = pd.DataFrame(helper.emoji_check(selected_user, df),columns=["Emoji", "How many times used?"])
    col1, col2,  = st.columns(2)
    with col1:
        st.dataframe(emoji_df, width=400)
    with col2:
        st.bar_chart(emoji_df.set_index('Emoji')['How many times used?'],)



    top_emoji = emoji_df.head(10)
    fig = px.pie(
        top_emoji,
        values='How many times used?',
        names='Emoji',
        title='Most Used Emojis')
    fig.update_layout(width=800,height=600)
    st.plotly_chart(fig)
    