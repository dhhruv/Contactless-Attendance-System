import os
import check_camera
import Capture_Image
import Train_Image
import Recognize


# Print the title bar
def title_bar():
    os.system("cls")
    print("\t**********************************************")
    print("\t***** Face Recognition Attendance System *****")
    print("\t**********************************************")


# Main menu
def main_menu():
    title_bar()
    print()
    print(10 * "*", "WELCOME MENU", 10 * "*")
    print("[1] Check Camera")
    print("[2] Capture Faces")
    print("[3] Train Images")
    print("[4] Recognize & Attendance")
    print("[5] Auto Mail")
    print("[6] Quit")

    try:
        choice = int(input("Enter Choice: "))
        print("\n")

        if choice == 1:
            check_camera.camer()
        elif choice == 2:
            Capture_Image.takeImages()
        elif choice == 3:
            Train_Image.TrainImages()
        elif choice == 4:
            Recognize.recognize_attendence()
        elif choice == 5:
            os.system("py automail.py")
        elif choice == 6:
            print("Thank You")
            return
        else:
            print("Invalid Choice. Enter 1-6")

        input("Press any key to return to main menu")
        main_menu()

    except ValueError:
        print("Invalid Choice. Enter 1-6\n Try Again")
        main_menu()


# Run the main menu
main_menu()
