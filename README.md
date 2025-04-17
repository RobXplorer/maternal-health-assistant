# 🤰 Maternal Health Assistant

An intelligent FastAPI backend + WhatsApp bot for assessing maternal health risks.

## 🔧 Backend

- Built with FastAPI
- Endpoint: `/predict`

## 📱 WhatsApp Bot

- Built with Flask + Twilio
- Parses user messages and interacts with the backend.

## 🚀 How to Run

### Backend:
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload

# WhatsApp Bot
cd whatsapp-bot
pip install -r requirements.txt
python app.py

# Make sure your FastAPI backend is running before using the bot.