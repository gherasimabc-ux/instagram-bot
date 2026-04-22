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
        "for a new camera to help me improve my photography!",
        "for a new camera to help me improve my photography",
        "for a new camera",
        "for a mackbook to edit my photosss",
        "for a new camera to help me improve my photography :>",
        "for a macbook for lightroom "
        
    ]

    message = messages[(day - 1) % len(messages)]

    return f"Day {day} of asking: {message}"
    
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
