import os
import json
from azure.communication.email import EmailClient

def send_email(sender, recipient, subject, text):
    connection_string = os.getenv('CONNECTION_STRING') or get_config('config.json', 'connection_string')

    client = EmailClient.from_connection_string(connection_string)

    message = {
        "senderAddress": sender,
        "recipients":  {
            "to": [{"address": recipient }],
        },
        "content": {
            "subject": subject,
            "plainText": text,
        }
    }


    print(message)

    poller = client.begin_send(message)
    return poller.result()

def get_config(file_path, key):
    with open(file_path, 'r') as f:
        config = json.load(f)
    return config[key]