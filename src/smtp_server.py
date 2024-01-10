from aiosmtpd.handlers import Message
from aiosmtpd.controller import Controller
from email import message_from_bytes

import azure_email

class CustomHandler(Message):
    def handle_message(self, message):
        subject = message.get('subject')
        senderAddresses = message.get('from')
        recipients = message.get('to')

        if message.is_multipart():
            for part in message.walk():
                if part.get_content_type() == 'text/plain':
                    charset = part.get_content_charset() if part.get_content_charset() else 'utf-8'
                    body = part.get_payload(decode=True).decode(charset)
        else:
            charset = message.get_content_charset() if message.get_content_charset() else 'utf-8'
            body = message.get_payload(decode=True).decode(charset)


        return azure_email.send_email(senderAddresses, recipients, subject, body);

def main():
    handler = CustomHandler()
    server = Controller(handler, hostname='0.0.0.0', port=1025)

    server.start()
    input("SMTP Relay Server started on %s at port %s. Press Return to quit." % (server.hostname, server.port))
    server.stop()

if __name__ == '__main__':
    main()