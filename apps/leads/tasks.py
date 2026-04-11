from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


print("EMAIL_BACKEND:", settings.EMAIL_BACKEND)
print("EMAIL_HOST_USER:", settings.EMAIL_HOST_USER)


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=5, max_retries=3)
def send_lead_email(self, name, email, phone, message):

    subject = "🔥 New Lead Received"

    content = f"""
🔥 New Lead Alert

👤 Name: {name}
📧 Email: {email}
📱 Phone: {phone}
📝 Message: {message}
"""

    send_mail(
        subject,
        content,
        settings.EMAIL_HOST_USER,   # 🔥 dynamic (best practice)
        [settings.EMAIL_HOST_USER],
        fail_silently=False,
    )