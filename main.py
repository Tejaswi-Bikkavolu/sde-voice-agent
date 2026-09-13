from fastapi import FastAPI
from twilio.rest import Client
import os

app = FastAPI()


@app.post("/webhook/send-whatsapp")
async def send_whatsapp(data: dict):

    summary = data.get(
        "summary",
        "Hot lead detected."
    )

    client = Client(
        os.getenv("TWILIO_ACCOUNT_SID"),
        os.getenv("TWILIO_AUTH_TOKEN")
    )

    whatsapp_body = f"""🔥 Hot Lead Detected

Hi, following up on our conversation.

{summary}

Thanks!
"""

    message = client.messages.create(
        from_=os.getenv("TWILIO_WHATSAPP_FROM"),
        to=os.getenv("TWILIO_WHATSAPP_TO"),
        body=whatsapp_body
    )

    return {
        "success": True,
        "message_sid": message.sid
    }


@app.post("/webhook/schedule-callback")
async def schedule_callback(data: dict):

    print("Callback requested:", data)

    return {
        "success": True,
        "message": "Callback scheduled",
        "callback_data": data
    }


@app.get("/")
async def root():
    return {"status": "SDE Voice Agent is running"}
