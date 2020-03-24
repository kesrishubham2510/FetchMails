import imaplib

def LogOut(ImapconnectionObject):
     ImapconnectionObject.close()
     ImapconnectionObject.logout()
     print('Logged out of the account successfully and securely')
     return