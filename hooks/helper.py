from django.core.mail import send_mail
from django.conf import settings


def send_admin_notification(user_data):

    subject = 'New User Signup Notification'
    message = f'New user signed up!\nUsername: {user_data.get("name")}\nEmail: {user_data.get("email")}'
    from_email = settings.DEFAULT_FROM_EMAIL
    print('from_email',from_email)
    recipient_list = user_data.get("email"),
    print('recipient_list',recipient_list)

    send_mail(subject, message, from_email, recipient_list)