import os
from imbox import Imbox # pip install imbox
import traceback
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--folder", help = "Show download_folder",type=str)
args = parser.parse_args()

host = "imap.gmail.com"
username = "amirilobna4@gmail.com"
password = '13051996*'
download_folder=args.folder
if not os.path.isdir(download_folder):
    os.makedirs(download_folder, exist_ok=True)
    
mail = Imbox(host, username=username, password=password, ssl=True, ssl_context=None, starttls=False)
messages = mail.messages(unread=True) 

for (uid, message) in messages:
    mail.mark_seen(uid) 

    for idx, attachment in enumerate(message.attachments):
        try:
            att_fn = attachment.get('filename')
            download_path = f"{download_folder}\{att_fn}"
            print(download_path)
            if ((att_fn.find('CV') !=-1) or (att_fn.find('cv') !=-1)) and ((os.path.splitext(att_fn)[1] == '.pdf') or (os.path.splitext(att_fn)[1] == '.doc') or (os.path.splitext(att_fn)[1] == '.docx')):
                
            
                with open(download_path, "wb") as fp:
                    fp.write(attachment.get('content').read())
        except:
            print(traceback.print_exc())

mail.logout()
