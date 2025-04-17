from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from parser import parse_message
from logger import log_message

app = Flask(__name__)

FASTAPI_URL = "http://localhost:8000/predict"  # update if deployed


@app.route("/whatsapp", methods=["POST"])
@app.route("/whatsapp", methods=["POST"])
def whatsapp_bot():
    sender = request.form.get("From")
    incoming_msg = request.form.get("Body").strip().lower()
    resp = MessagingResponse()

    try:
        # Greet or help
        if incoming_msg in {"hi", "hello", "help", "start"}:
            reply = (
                "👋 Welcome to the Maternal Health Assistant!\n\n"
                "To assess your health, send a message like:\n"
                "`bp 140/90 fever yes bleeding no headache no convulsions no`\n\n"
                "Respond with `yes` or `no` after each symptom.\n"
                "We'll give you a risk level and recommendation instantly 💡"
            )
        else:
            user_data = parse_message(incoming_msg)
            res = requests.post(FASTAPI_URL, json=user_data)
            result = res.json()
            reply = f"Risk: {result['risk_level'].upper()}\nAdvice: {result['recommendation']}"

    except ValueError as ve:
        reply = f"⚠️ Error: {ve}"
    except Exception:
        reply = "⚠️ Something went wrong. Please check your input format and try again."

    log_message(sender, incoming_msg, reply)
    resp.message(reply)
    return str(resp)


if __name__ == "__main__":
    app.run(port=5000)