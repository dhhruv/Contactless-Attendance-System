import os
import time
import cv2
import numpy as np
from PIL import Image
from threading import Thread


def get_images_and_labels(path):
    """
    Function to load images and labels from the given path.
    """
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    faces = []
    ids = []

    for image_path in image_paths:
        pil_image = Image.open(image_path).convert("L")
        image_np = np.array(pil_image, "uint8")
        id = int(os.path.split(image_path)[-1].split(".")[1])
        faces.append(image_np)
        ids.append(id)

    return faces, ids


def train_images():
    """
    Function to train images for face recognition.
    """
    recognizer = cv2.face_LBPHFaceRecognizer.create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    faces, id = get_images_and_labels("TrainingImage")

    # Start threads for training and optional image counter
    Thread(target=recognizer.train, args=(faces, np.array(id))).start()
    Thread(target=counter_img, args=("TrainingImage",)).start()

    recognizer.save("TrainingImageLabel/Trainner.yml")
    print("All Images Trained")


def counter_img(path):
    """
    Optional function to count the number of trained images.
    """
    img_counter = 1
    image_paths = [os.path.join(path, f) for f in os.listdir(path)]
    for _ in image_paths:
        print(f"{img_counter} Images Trained", end="\r")
        time.sleep(0.008)
        img_counter += 1


if __name__ == "__main__":
    train_images()
