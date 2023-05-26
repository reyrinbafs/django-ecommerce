
from django.conf import settings
from django.core.mail import send_mail


def send_email_verification(email, email_token):
    subject = "Your account needs to be verified."
    email_from = settings.EMAIL_HOST_USER
    message = f"Hi, Click on the link to acticate your account http://127.0.0.1:8000/accounts/activate/{email_token}"
    send_mail(subject, message, email_from, [email])