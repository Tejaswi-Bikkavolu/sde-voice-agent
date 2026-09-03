from fastapi import FastAPI

app = FastAPI()

@app.post("/webhook/send-whatsapp")
async def send_whatsapp(data: dict):
    print("Received from Retell:", data)

    return {
        "success": True,
        "message": "WhatsApp action received"
    }