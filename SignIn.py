import imaplib

def Login(imapHost, userId, passCode):

    connection= imaplib.IMAP4_SSL(imapHost)
    connection.login(userId, passCode)
    print('Logged in the account successfully', '\n')
    connection.select('Inbox', readonly=True) #selecting inbox to iterate and search the emails
    return connection

