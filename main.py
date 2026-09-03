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
        to=os.getenv("TWILIO_WHATSAPP_TO"),
        content_sid="HX7cf5a23fe00549e2ed931e272889fb49"
    )

    return {
        "success": True,
        "message_sid": message.sid
    }
