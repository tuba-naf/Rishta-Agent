import chainlit as cl
from agents.function_tool import function_tool
import requests
import os

@function_tool
def send_whatsapp_message(number: str, message: str) -> str:
    """
    Uses the UltraMSG API to send a custom WhatsApp message to the specified phone number.
    Returns a success message if sent successfully, or an error message if the request fails.
    """

    instance_id = os.getenv("INSTANCE_ID")
    token = os.getenv("API_TOKEN")

    if not instance_id or not token:
        return "❌ Missing INSTANCE_ID or API_TOKEN in environment variables."

    if not number or not message:
        return "❌ Phone number and message cannot be empty."

    url = f"https://api.ultramsg.com/{instance_id}/messages/chat"
    
    payload = {
        "token": token,
        "to": number,
        "body": message
    }

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        result = response.json()
        if result.get("sent"):
            return f"📤 Message sent successfully to {number}"
        else:
            return f"❌ Message not sent. Server response: {result}"
    else:
        return f"❌ Failed to send message. HTTP {response.status_code}: {response.text}"
