import datetime
import os
import cv2
import pandas as pd


def recognize_attendance():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read("TrainingImageLabel" + os.sep + "Trainner.yml")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    df = pd.read_csv("EmployeeDetails" + os.sep + "EmployeeDetails.csv")
    font = cv2.FONT_HERSHEY_SIMPLEX
    col_names = ["Id", "Name", "Time"]
    attendance = pd.DataFrame(columns=col_names)

    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height

    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)

    minThreshold = 40

    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray, 1.2, 5, minSize=(int(minW), int(minH)), flags=cv2.CASCADE_SCALE_IMAGE
        )

        for x, y, w, h in faces:
            cv2.rectangle(im, (x, y), (x + w, y + h), (10, 159, 255), 2)
            Id, conf = recognizer.predict(gray[y : y + h, x : x + w])

            if conf < 100:
                name = df.loc[df["Id"] == Id]["Name"].values
                confstr = "  {0}%".format(round(100 - conf))
                tt = f"{str(Id)}-{name}"

            else:
                tt = "  Unknown"
                confstr = "  {0}%".format(round(100 - conf))

            if (100 - conf) > minThreshold:
                timeStamp = datetime.datetime.fromtimestamp(time.time()).strftime(
                    "%H:%M:%S"
                )
                name = str(name)[2:-2]

                attendance.loc[len(attendance)] = [Id, name, timeStamp]
                tt = tt + " [Pass]"
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            else:
                cv2.putText(im, str(tt), (x + 5, y - 5), font, 1, (255, 255, 255), 2)

            if (100 - conf) > minThreshold:
                cv2.putText(
                    im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 0), 1
                )
            elif (100 - conf) > 50:
                cv2.putText(
                    im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 255, 255), 1
                )
            else:
                cv2.putText(
                    im, str(confstr), (x + 5, y + h - 5), font, 1, (0, 0, 255), 1
                )

        attendance = attendance.drop_duplicates(subset=["Id"], keep="first")
        cv2.imshow("Attendance", im)
        if cv2.waitKey(1) == ord("q"):
            break

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    fileName = "Attendance" + os.sep + "Attendance_" + date + ".csv"
    file_path = os.path.join(os.getcwd(), fileName)
    if os.path.exists(file_path):
        old_file = pd.read_csv(file_path)
        combined_file = pd.concat([old_file, attendance])
        combined_file.drop_duplicates(subset=["Id"], keep="first", inplace=True)
        combined_file.to_csv(fileName, index=False)
    else:
        attendance.to_csv(fileName, index=False)

    print("Attendance Successful")
    cam.release()
    cv2.destroyAllWindows()
