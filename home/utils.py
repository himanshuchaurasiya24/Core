from .models import Student
import time
from django.core.mail import send_mail
from django.conf import settings
def run_this_function():
    print('Run this functions')
    time.sleep(1)
    print('Function exit')
    # time.sleep(1)
def send_email_to_client():
    subject ="this email is from django server"
    message="this is a test message from django server email"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['himanshuchaurasiya24@gmail.com']
    send_mail(subject, message, from_email, recipient_list)

