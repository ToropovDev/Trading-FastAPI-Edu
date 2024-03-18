import smtplib
from email.message import EmailMessage

from celery import Celery
from ..config import SMTP_USER, SMTP_PASSWORD

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

'''
run celery

celery -A src.tasks.tasks:celery_app worker --loglevel=INFO --pool=solo
celery -A src.tasks.tasks.celery_app flower
'''


celery_app = Celery("tasks", broker="redis://localhost:6379")


def get_email_template_dashboard(username: str, user_email: str):
    email = EmailMessage()
    email['Subject'] = "Dashboard"
    email['From'] = SMTP_USER
    email['To'] = user_email

    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        '-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app'
        '-mobile-free-vector.jpg" width="600">'
        '</div>',
        subtype='html'
    )
    return email


@celery_app.task
def send_email_dashboard(username: str, user_email: str):
    email = get_email_template_dashboard(username, user_email)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)

