from datetime import datetime

def log_message(sender, message, response):
    with open("messages.log", "a", encoding="utf-8") as f:
        f.write(f"{datetime.now()} | From: {sender} | Msg: {message} | Response: {response}\n")
