from fastapi import FastAPI
from twilio.rest import Client
import os

app = FastAPI()


# -----------------------------
# HOT LEAD → SEND WHATSAPP
# -----------------------------
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


# -----------------------------
# WARM LEAD → SCHEDULE CALLBACK
# -----------------------------
callbacks = []


@app.post("/webhook/schedule-callback")
async def schedule_callback(data: dict):

    callback_time = data.get("callback_time")
    phone_number = data.get("phone_number")
    reason = data.get("reason")

    callback = {
        "callback_time": callback_time,
        "phone_number": phone_number,
        "reason": reason
    }

    callbacks.append(callback)

    print("CALLBACK BOOKED:", callback)

    return {
        "success": True,
        "message": "Callback booked successfully",
        "callback": callback
    }
