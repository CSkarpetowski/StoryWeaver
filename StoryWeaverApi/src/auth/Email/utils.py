from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from src.auth.Email.models import EmailSchema
from jinja2 import Environment, FileSystemLoader, select_autoescape
from fastapi.templating import Jinja2Templates
from decouple import config

env = Environment(loader=FileSystemLoader('src/auth/Email/templates'),
                  autoescape=select_autoescape(['html', 'xml']))

user = config('GOOGLE_USERNAME')
password = config('GOOGLE_PASSWORD')
port = config('GOOGLE_PORT')
server = config('GOOGLE_HOST')
mail = config('GOOGLE_MAIL_FROM')

conf = ConnectionConfig(
    MAIL_USERNAME=mail,
    MAIL_PASSWORD=password,
    MAIL_FROM=mail,
    MAIL_PORT=port,
    MAIL_SERVER=server,
    MAIL_FROM_NAME="noreply.StoryWeaver",
    MAIL_SSL_TLS=False,
    MAIL_STARTTLS=True,
    USE_CREDENTIALS=True
)


async def send_email(email: EmailSchema, template_name: str, context: dict):
    body = get_template(template_name, context)
    message = MessageSchema(
        subject=email.subject,
        recipients=[email.email],
        body=body,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)


def get_template(template_name: str, context: dict):
    template = env.get_template(template_name)
    body = template.render(**context)
    return body
