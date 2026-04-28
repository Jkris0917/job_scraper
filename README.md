# 🤖 Job Scraper Bot + Web

A full-stack job aggregator that automatically scrapes job listings from multiple platforms (Jobstreet, Kalibrr, etc.) and displays them through a modern web interface.

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python |
| Database | MySQL |
| Frontend | React + TypeScript + Tailwind CSS |

---

## 📁 Project Structure

```
job_scraper/
├── scrapers/
│   ├── __init__.py
│   ├── base.py          # Base scraper class
│   ├── jobstreet.py     # Jobstreet scraper
│   └── kalibrr.py       # Kalibrr scraper
├── venv/                # Virtual environment (not committed)
├── .env                 # Environment variables (not committed)
├── .env.example         # Environment variable template
├── database.py          # Database connection & queries
├── models.py            # Data models
├── requirements.txt     # Python dependencies
└── README.md
```

---

## ⚙️ Prerequisites

- Python 3.9+
- Node.js 18+
- MySQL 8.0+
- Git

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/job_scraper.git
cd job_scraper
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables

Copy `.env.example` to `.env` and fill in your values:

```bash
cp .env.example .env
```

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=job_scraper_db
DB_USER=your_db_user
DB_PASSWORD=your_db_password
```

### 4. Database Setup

```bash
# Create the MySQL database
mysql -u root -p

# Inside MySQL shell
CREATE DATABASE job_scraper_db;
exit;

# Run migrations
python database.py
```

### 5. Run the Scraper

```bash
python main.py
```

### 6. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

---

## 🕷️ Scrapers

| Platform | File | Status |
|---|---|---|
| Jobstreet | `scrapers/jobstreet.py` | ✅ Active |
| Kalibrr | `scrapers/kalibrr.py` | ✅ Active |

---

## 📬 Telegram Bot Features

The bot is integrated with Telegram to keep you updated in real time.

| Feature | Description |
|---|---|
| 📢 New Job Alerts | Instantly notifies you when a new job listing is scraped |
| 📋 Daily Digest | Sends a summary of all scraped jobs every day |
| ⚠️ Error Notifications | Alerts you when a scraper encounters an error or fails |
| 🔍 Job Search | Send a keyword to the bot and it replies with matching job listings |

### Telegram Setup

1. Create a bot via [@BotFather](https://t.me/BotFather) on Telegram
2. Copy your **Bot Token**
3. Get your **Chat ID** (use [@userinfobot](https://t.me/userinfobot))
4. Add them to your `.env` file:

```env
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_CHAT_ID=your_chat_id_here
```

### Bot Commands

| Command | Description |
|---|---|
| `/search <keyword>` | Search jobs by keyword |
| `/digest` | Manually trigger today's job digest |
| `/status` | Check scraper status |

---

## 🌐 Frontend

- Built with **React + TypeScript**
- Styled with **Tailwind CSS**
- Displays scraped job listings with filters by platform, location, and job title

---

## 📦 Backend Dependencies

See `requirements.txt`. Key packages:

```
requests
beautifulsoup4
selenium
mysql-connector-python
python-dotenv
python-telegram-bot
```

---

## 🔒 Environment Variables Reference

| Variable | Description |
|---|---|
| `DB_HOST` | MySQL host (e.g. `localhost`) |
| `DB_PORT` | MySQL port (default `3306`) |
| `DB_NAME` | Database name |
| `DB_USER` | Database username |
| `DB_PASSWORD` | Database password |
| `TELEGRAM_BOT_TOKEN` | Your Telegram bot token from @BotFather |
| `TELEGRAM_CHAT_ID` | Your Telegram chat/user ID |

---

## 🛠️ Development Notes

- Never commit `.env` — use `.env.example` as a template
- `venv/` is excluded from Git
- Each scraper extends `base.py` for consistency

---

## 📄 License

MIT License — feel free to use and modify.

---

## 👤 Author

John Kris Gellado — [@jkris0917](https://github.com/jkris0917)