from aiosmtpd.handlers import Message
from aiosmtpd.controller import Controller

import azure_email

class AzureEmailHandler(Message):
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
    handler = AzureEmailHandler()
    server = Controller(handler, hostname='0.0.0.0', port=1025)

    try:
        server.start()
        print("SMTP Relay Server started on %s at port %s. Press Ctrl+C to quit." % (server.hostname, server.port))
        while True:
            pass
    except KeyboardInterrupt:
        print("SMTP Relay Server is stopping...")
        server.stop()
    

if __name__ == '__main__':
    main()