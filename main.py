from fastapi import FastAPI
from twilio.rest import Client
import os

app = FastAPI()

@app.post("/webhook/send-whatsapp")
async def send_whatsapp(data: dict):

    summary = data.get("summary", "Hot lead detected.")

    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

    message = client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to="whatsapp:YOUR_NUMBER",
        body=f"🔥 HOT LEAD\n\n{summary}"
    )

    return {
        "success": True,
        "message_sid": message.sid
    }
