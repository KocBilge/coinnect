# app/tasks.py
from .celery_config import celery_app

@celery_app.task
def send_email(email: str, subject: str, body: str):
    # Simulate sending an email
    print(f"Sending email to {email} with subject '{subject}'")
    return True
