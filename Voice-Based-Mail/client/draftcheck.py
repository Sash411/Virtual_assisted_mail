import imaplib
from email.message import EmailMessage

def save_draft_email(subject, toaddr, body):
    # Connect to the IMAP server
    imap_server = imaplib.IMAP4_SSL('imap.gmail.com')

    try:
        # Login to the Gmail account
        email = 'rapid1056@gmail.com'
        password = 'khnfmaoozglbbqzx'

        imap_server.login(email, password)

        # Select the 'INBOX' mailbox
        imap_server.select("[Gmail]/Drafts")

        # Create the email message
        message = EmailMessage()
        message['Subject'] = subject
        message['From'] = email
        message['To'] = toaddr
        message.set_content(body)
        imap_server.append("[Gmail]/Drafts", '', None, message.as_bytes())

        

        print("Email saved as draft in Gmail")

    finally:
        # Logout and close the IMAP connection
        imap_server.logout()




