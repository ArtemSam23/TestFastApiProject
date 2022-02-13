import smtplib
from email.message import EmailMessage
from email_app.email_config import EMAIL_USER, EMAIL_PASS, HOST, PORT
from sql_app.schemas import UserCreate


def send_signup_confirmation(user: UserCreate | None = None, __test=False):
    if __test:
        address = "artemsam23@gmail.com"
        password = 'myPassword'
    else:
        address = user.email
        password = user.password

    msg = EmailMessage()
    msg['Subject'] = "Signup confirmation"
    msg['From'] = EMAIL_USER
    msg['To'] = address
    msg.set_content("You have been signed up.\nPassword: {password}".format(password=password))

    with smtplib.SMTP_SSL(host=HOST, port=PORT) as s:
        s.login(user=EMAIL_USER, password=EMAIL_PASS)
        s.send_message(msg)
        print('Email was successfully sent.')


if __name__ == '__main__':
    send_signup_confirmation(__test=True)
