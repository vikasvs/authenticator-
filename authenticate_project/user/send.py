#!/usr/bin/python3

# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

DEFAULT_FROM_EMAIL = "kurnoolsaketh@gmail.com"

HIRING_SAMPLE_CONTENT = "<strong>TEST HIRING MANAGER EMAIL</strong>"

KEY = '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' # TODO: make this env variable
def send(to, subject, content):
    message = Mail(
        from_email=DEFAULT_FROM_EMAIL,
        to_emails=to,
        subject=subject,
        html_content=content)
    try:
        sg = SendGridAPIClient(KEY)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)