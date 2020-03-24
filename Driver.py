import SignIn
import SignOut
import Display
import Verify


userId= input('Enter your Email_Id')
passCode= input('Enter your passCode')
imapHost= 'imap.gmail.com' #for gmail

connect= SignIn.Login(imapHost, userId, passCode)
search= input('Enter the Inquiring Email id')

if Verify.verifier(search)=='OK':
    Display.findMails('FROM', search, connect)

else:
    print('U Entered a wrong Email Id/Address')
    search = input('Enter the Inquiring Email id again carefully and attentively')
    if Verify.verifier(search) == 'OK':
        Display.findMails('FROM', search, connect)
    else:
        print('Unsuccessfull Attempts Try Later!!')
        SignOut.LogOut()

SignOut.LogOut(connect)


