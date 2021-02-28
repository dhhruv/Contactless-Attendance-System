import yagmail
import os
import datetime
import Info
import pandas as pd
import numpy as np

date = datetime.date.today().strftime("%B %d, %Y")
path = 'Attendance'
os.chdir(path)
files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
# receiver = 'neelcshah1012@gmail.com'
# receiver = 'payaldevalia1111@gmail.com'
df = pd.read_csv(r'EmployeeDetails\EmployeeDetails.csv')   
        
receivers = df["email"]
newest = files[-1]
filename = newest
sub = "Attendance Report for " + str(date)
body = " Attendance Submitted."

for receiver in receivers:
    # receiver = 'nirjadesai9800@gmail.com'
    # mail information
    if pd.isnull(reciver):
        continue
    else:
        yag = yagmail.SMTP(Info.EMAIL_ID, Info.PASSWORD)

        # sent the mail
        yag.send(
            to=receiver,
            subject=sub, # email subject
            contents=body,  # email body
            attachments= filename  # file attached
        )
        print("Email Sent to "+reciver)
