import pyautogui
from time import sleep
import sys

# the basic welcome message

def welcome():
    print("\t==>> THE BEAN BOT <<==")
    print()


# to check if the user wants to spam from a txt file or a word/sentence

def get_spam_type():
    print("Spam a word/sentence - enter 1")
    print("Spam from a text file - enter 2")
    spam_type = int(input('Enter your choice: '))
    return spam_type


# to get the speed of how fast it should spam
# in simple words, it returns the time after
# which the next spam message has to be sent

def get_spam_speed():
    print()
    print("=== SPAM SPEED speed (seconds) ===")
    print("Super fast = Enter 0")
    print("Medium speed = Enter 0.7")
    print("Or set your custom speed: ")
    print()
    spam_speed = float(input("Enter your speed: "))
    return spam_speed


def get_timeout_and_timeout():
    timeout = float(input("Enter the time you need to open the app and focus the cursor on:"))
    print("HURRY UP AND PLACE YOUR CURSOR WITHIN", timeout, "SECONDS!!")
    sleep(timeout)


def get_spam_text():
    text = input("Enter what you want to spam: ")
    return text


def spam_text(spam_speed, num_of_times, text):
    print("Spamming...")
    i = 0

    while i < num_of_times:
        pyautogui.typewrite(text)
        pyautogui.press("enter")
        sleep(float(spam_speed))
        i += 1


def quit():
    print("BEAN the bot quits...")
    sys.exit()


def main():
    welcome()
    spam_type = get_spam_type()
    spam_speed = get_spam_speed()

    if spam_type == 1:
        def get_num_of_times():
            # word or sentence entered by user
            num_of_times = float(input("Enter number of times to spam: "))
            return num_of_times

        text = get_spam_text()
        num_of_times = get_num_of_times()
        get_timeout_and_timeout()
        spam_text(spam_speed, num_of_times, text)
        quit()

    elif spam_type == 2:  # to spam from a text file

        def spam_from_file(spam_speed):
            file_name = str(
                input("Enter the name of the file (eg. spam_text.txt): "))
            print("NOTE: Text file has to be in same folder/directory")
            print("NOTE: Currently only text files are supported!")
            get_timeout_and_timeout()
            try:
                text_file = open(file_name, "r")
                for line in text_file:
                    pyautogui.typewrite(line)
                    pyautogui.press("enter")
                    sleep(spam_speed)
            except:
                print("File not found or file name incorrect")
                quit()

        spam_from_file(spam_speed)
    else:
        quit()


# calling the main function
try:
    main()
except:
    print("Invalid Input/Something went wrong. Please try again!")
    quit()
