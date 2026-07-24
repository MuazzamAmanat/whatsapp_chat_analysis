<div align="center">

# 📊 WhatsApp Chat Analyzer

### Turn your WhatsApp conversations into beautiful, actionable insights.

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=flat&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)

**[🔗 Live Demo](https://whatsapp-chat-analysis1.streamlit.app/)** &nbsp;•&nbsp; **[📖 How It Works](#-how-to-use)** &nbsp;•&nbsp; **[🛠️ Tech Stack](#️-tech-stack)**

</div>

---

Ever wondered who *really* dominates your group chat? Or what time of day your friends go silent? **WhatsApp Chat Analyzer** takes your exported chat history and transforms it into a rich, interactive dashboard — no data science degree required.

Just upload a `.txt` export, pick a user (or view everyone), and let the app reveal the story hidden in your messages: activity streaks, favorite words, emoji obsessions, and more.

## 🔗 Live Demo

**App URL:** `https://whatsapp-chat-analysis1.streamlit.app/`

> ⚠️ **First-load styling issue:** On some browsers, the very first click can render an unstyled/plain page (missing fonts, missing button styling). This is a known Streamlit Community Cloud caching quirk, not a broken link.
> **Fix:** Hard-refresh the page once — `Ctrl+Shift+R` (Windows/Linux) or `Cmd+Shift+R` (Mac) — and it will load normally. After that first refresh, it stays fixed for future visits.

## ✨ Features

| Category | What you get |
|---|---|
| 📌 **Overview** | Total messages, total words, media shared, links shared |
| 👥 **User Insights** | Most active members, individual user deep-dive, contribution percentage |
| 📈 **Trends** | Monthly message timeline, last-30-days daily activity |
| 🔥 **Activity Patterns** | Busiest days, busiest months, member activity heatmaps |
| ☁️ **Text Analysis** | Word cloud, most frequent words, smart stopword filtering |
| 😀 **Emoji Analysis** | Top emojis, frequency table, distribution pie chart |

## 🛠️ Tech Stack

Built with a lean, battle-tested Python data stack:

| Layer | Tools |
|---|---|
| Web App | Streamlit |
| Data Processing | Pandas, Regex |
| Visualization | Matplotlib, Plotly, WordCloud |
| Text/Emoji Parsing | Emoji Library |

## 📂 Project Structure

```
whatsapp_chat_analysis/
│
├── app.py                 # Streamlit application
├── preprocessor.py        # Chat preprocessing and cleaning
├── helper.py               # Analysis functions
├── romanEng2.csv           # Custom stopwords file
├── requirements.txt        # Project dependencies
└── README.md
```

## 🚀 Getting Started

### Option 1: Use it instantly (no setup)

Open the live app at `https://whatsapp-chat-analysis1.streamlit.app/` and start uploading your chat right away.
*(Remember: hard-refresh once if the page looks unstyled on first load — see [Live Demo](#-live-demo) note above.)*

### Option 2: Run it locally

Clone the repository:

```bash
git clone https://github.com/MuazzamAmanat/whatsapp_chat_analysis.git
```

Navigate to the project folder:

```bash
cd whatsapp_chat_analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## 📱 How to Use

**1. Export your WhatsApp chat**
   - Open WhatsApp → select a chat or group
   - Tap **⋮ (More options) → More → Export chat**
   - Choose **Without Media**
   - Save the resulting `.txt` file

**2. Upload it** into the app (locally or via the live demo above)

**3. Choose your view**
   - 🌐 Overall group analysis
   - 👤 Specific user analysis

**4. Explore** — scroll through interactive charts, word clouds, and emoji breakdowns

## 📊 Questions It Can Answer

- 🏆 Who is the most active member of the group?
- 📅 Which day of the week is everyone most chatty?
- 📆 What month had the highest message volume?
- 🔤 Which words come up again and again?
- 😂 Which emojis dominate the conversation?

## 🔒 Privacy First

All processing happens within the app itself — your chat is never stored or shared. That said, as good practice, avoid uploading sensitive personal conversations to public/shared environments.

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/MuazzamAmanat/whatsapp_chat_analysis/issues) or open a pull request.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👨‍💻 Author

**Muazzam Amanat**

[![GitHub](https://img.shields.io/badge/GitHub-MuazzamAmanat-181717?style=flat&logo=github)](https://github.com/MuazzamAmanat/whatsapp_chat_analysis)

---

<div align="center">

If you found this project useful, consider giving it a ⭐ on GitHub!

</div>
