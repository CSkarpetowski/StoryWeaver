from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from src.auth.Email.models import EmailSchema
from jinja2 import Environment, FileSystemLoader, select_autoescape
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="src/auth/Email/templates")

conf = ConnectionConfig(
    MAIL_USERNAME="username",
    MAIL_PASSWORD="**********",
    MAIL_FROM="test@email.com",
    MAIL_PORT=587,
    MAIL_SERVER="mail server",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True
)


async def send_email(email: EmailSchema, template_name: str, context: dict):
    body = get_template(template_name, context)
    message = MessageSchema(
        subject=email.subject,
        recipients=email.email,
        body=body,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)


def get_template(template_name: str, context: dict):
    env = Environment(loader=FileSystemLoader('templates'),
                      autoescape=select_autoescape(['html', 'xml'])
                      )
    template = env.get_template(template_name)
    body = template.render(**context)
    return body
