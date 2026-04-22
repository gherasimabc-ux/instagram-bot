from datetime import datetime
import random
import time
from instagrapi import Client

import os

USERNAME = os.getenv("IG_USERNAME")
PASSWORD = os.getenv("IG_PASSWORD")

TARGET_USERS = ["carterpcs_"]

START_DATE = datetime(2026, 4, 22)

def get_day_number():
    today = datetime.now()
    delta = today - START_DATE
    return delta.days + 1

def generate_message():
    day = get_day_number()

    messages = [
        "for a new camera to improve my photography",
        "for a new camera so I can get better at photography",
        "for a camera to keep improving my photos",
        "for a better camera for my photography",
        "for a new camera, trying to get better at this",
        
        "for a macbook to edit my photos",
        "for a macbook so I can edit properly",
        "for a macbook for editing my photos",
        "for a macbook to work on my photos",
        
        "for a camera, I really want to improve",
        "for a camera to take better photos",
        "for a camera so I can keep learning",
        
        "for a macbook for lightroom",
        "for a macbook to use lightroom properly",
        "for a macbook so I can edit in lightroom",
        
        "for a new camera, still working on my photography",
        "for a camera, just trying to get better each day",
        
        "for a macbook, need it for editing",
        "for a macbook to make editing easier",
        
        "for a new camera :>",
        "for a camera, slowly getting into photography",
        
        "for a macbook haha",
        "for a macbook, I need it for my photos",
        
        "for a new camera, I really want to take this seriously",
        "for a camera to improve my shots",
        
        "for a macbook, editing would be way easier",
        "for a macbook so I can actually edit my photos properly"
    ]

    base_message = messages[(day - 1) % len(messages)]

    # tiny human-like variations
    extras = ["", ".", " haha", " :>", " fr", " lol", " tbh"]
    ending = random.choice(extras)

    return f"Day {day} of asking: {base_message}{ending}"
    
def wait_random_time():
    delay = random.randint(0, 3600)
    time.sleep(delay)

def send_messages():
    cl = Client()
    cl.login(USERNAME, PASSWORD)

    message = generate_message()

    for user in TARGET_USERS:
        user_id = cl.user_id_from_username(user)
        cl.direct_send(message, [user_id])
        print("Sending message:", message)
        print("Message sent!")

if __name__ == "__main__":
 #   wait_random_time()
 print("Starting bot...")
send_messages()
