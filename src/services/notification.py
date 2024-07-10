import os
import smtplib
import ssl
from email.message import EmailMessage
import time
import pygame


def play_visa_alarm():
    try:
        pygame.mixer.init()
        sound_file = './src/static/mp3/mixkit-police-siren-us-1643.mp3'
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play(loops=-1)
        time.sleep(60)
        pygame.mixer.music.stop()
    except Exception as e:
        print(f"Error playing notification sound: {e}")

def send_visa_notification(team: str):
    try:
        email_sender = os.environ.get("EMAIL_SENDER")
        email_password = os.environ.get("EMAIL_PASSWORD")
        email_receiver = os.environ.get("EMAIL_RECEIVER")
                
        if not email_password:
            raise ValueError("Email password not found in environment variables")

        subject = "Horarios disponiveis para o Visto"
        body = f"Aparentemente novos horários estão disponíveis no time {team}, por favor checar o link: https://termine.staedteregion-aachen.de/auslaenderamt/select2?md=1"

        message = EmailMessage()
        message.set_content(body)
        message["Subject"] = subject
        message["From"] = email_sender
        message["To"] = email_receiver

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.send_message(message)
        
        print("Email notification sent successfully.")
    except Exception as e:
        print(f"Failed to send email notification: {e}")
