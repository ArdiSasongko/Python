import threading
import string
import time

def print_numbers():
    for i in range(1,11):
        print("thread number :", i)
        time.sleep(0.5)

letters = list(string.ascii_uppercase[:11])
def print_letters():
    for i in letters:
        print("thread Letters : ", i)
        time.sleep(0.5)

number = threading.Thread(target=print_numbers)
letter = threading.Thread(target=print_letters)

number.start()
letter.start()

number.join()
letter.join()