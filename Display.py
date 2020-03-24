import email
import datetime
import imaplib
import email.header

def findMails(key,value,connection):
    status, results= connection.search(None, 'FROM', '"{}"'.format(value)) #searching all mails from value

    if status!='OK':
        print("No Emails from ", value, " Account")
        return
    else:
        print('U have Received ', (results[0].split()).__len__(), 'mails from ', value)

    for num in results[0].split():
       status, rawByte = connection.fetch(num, "(RFC822)")
       RawBytes= rawByte[0][1].decode('utf-8') #decoding the byte message as per 'utf-8' standards
       RawEmail= email.message_from_string(RawBytes)
       getDetails(num, RawEmail)
       print('\n\n')

    return

def getDetails(num, rawEmail):

    print("Messaged To: ", rawEmail['To'], " From: ", rawEmail['From'])
    hdr= email.header.make_header(email.header.decode_header(rawEmail['Subject']))
    subject = str(hdr)
    print('Message %s: %s' % (num, subject)) #"b'xyz" b symbolises byte
    print('Raw Date : ', rawEmail['Date'])

    #converting to local Date-time
    date_tuple= email.utils.parsedate_tz(rawEmail['Date'])
    if date_tuple:
        local_date= datetime.datetime.fromtimestamp(email.utils.mktime_tz(date_tuple))
        print('Local Date : ', local_date.strftime("%a, %d %b %Y %H:%M:%S"))

    return
