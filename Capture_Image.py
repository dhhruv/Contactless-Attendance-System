import csv
import re
import cv2
import os
from unicodedata import numeric


def is_number(value):
    """
    Function to check if a value is numeric.
    """
    try:
        float(value)
        return True
    except ValueError:
        pass

    try:
        numeric(value)
        return True
    except (TypeError, ValueError):
        pass

    return False


def validate_email(email):
    """
    Function to validate an email using regex.
    """
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    return re.search(regex, email)


def save_image(Id, name, email, gray, x, y, w, h):
    """
    Function to save image and data.
    """
    cv2.imwrite(
        f"TrainingImage/{name}.{Id}.{sampleNum}.jpg", gray[y : y + h, x : x + w]
    )
    with open("EmployeeDetails/EmployeeDetails.csv", "a+") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow([Id, name, email])


def capture_images(Id, name, email):
    """
    Function to capture images.
    """
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    sampleNum = 0

    while True:
        ret, img = cam.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(
            gray, 1.3, 5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE
        )
        for x, y, w, h in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (10, 159, 255), 2)
            sampleNum += 1
            save_image(Id, name, email, gray, x, y, w, h)
            cv2.imshow("frame", img)
        if cv2.waitKey(100) & 0xFF == ord("q") or sampleNum > 100:
            break

    cam.release()
    cv2.destroyAllWindows()


def takeImages(Id, name, email):
    """
    Main function to validate data and start image capturing process.
    """
    if is_number(Id) and validate_email(email):
        capture_images(Id, name, email)
        print(
            f"Images Saved for ID : {Id} Name : {name.replace(' ', '')} Email : {email}"
        )
    else:
        if not is_number(Id):
            print("Enter Alphabetical Name")
        else:
            print("Enter correct email address")
