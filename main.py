import chainlit as cl

@cl.on_chat_start
async def start():
    cl.user_session.set("history", [])
    await cl.Message("Salam beta! Main *Rishty Wali Auntie* hoon. Apna rishta batain, age batain, aur WhatsApp number dein. 😄").send()

def get_user_data(min_age: int) -> list[dict]:
    users = [
        {"name": "Maisam", "age": 17},
        {"name": "Jahanzeb", "age": 25},
        {"name": "Mohsin", "age": 19},
        {"name": "Ibrahim", "age": 24},
        {"name": "Salar", "age": 22},
    ]
    return [user for user in users if user["age"] >= min_age]

@cl.on_message
async def main(message: cl.Message):
    content = message.content.strip()
    await cl.Message("Thinking...").send()

    try:
        age = int(content)
        matches = get_user_data(age)
        if matches:
            names = ", ".join([user["name"] for user in matches])
            reply = f"Beta {age} saal ka hai? Yeh rishtay munasib lagtay hain: {names} 💍"
        else:
            reply = f"Beta {age} saal mein aunty ko koi rishta nahi mila 😢"
    except ValueError:
        if "whatsapp" in content.lower() or content.startswith("03") or "number" in content.lower():
            reply = "Shukriya beta, number mil gaya. Ab aunty ka kaam start! ☎️"
        else:
            reply = "Beta sirf umar ya WhatsApp number bhejo, aunty confused ho gayi 😅"

    await cl.Message(reply).send()
