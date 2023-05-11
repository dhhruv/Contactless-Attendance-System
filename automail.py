import os
import datetime
import yagmail
import pandas as pd
from Info import EMAIL_ID, PASSWORD


def send_email(receiver, subject, body, filename):
    yag = yagmail.SMTP(EMAIL_ID, PASSWORD)

    yag.send(to=receiver, subject=subject, contents=body, attachments=filename)
    print(f"Email Sent to {receiver}")


def main():
    date = datetime.date.today().strftime("%B %d, %Y")
    path = "Attendance"
    os.chdir(path)
    files = sorted(os.listdir(), key=os.path.getmtime)

    df = pd.read_csv(r"EmployeeDetails\EmployeeDetails.csv")
    receivers = df["email"]

    newest_file = files[-1]
    subject = "Attendance Report for " + date
    body = "Attendance Submitted."

    for receiver in receivers:
        if pd.isnull(receiver):
            continue
        else:
            send_email(receiver, subject, body, newest_file)


if __name__ == "__main__":
    main()
