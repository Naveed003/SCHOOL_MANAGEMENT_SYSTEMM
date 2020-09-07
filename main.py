from datetime import date
import sqlite3
import pandas as pd
import time
import random
from random import randint
from datetime import datetime
import os
mydb = sqlite3.connect("database.db")
mycursor = mydb.cursor()


def clr_screen():
    if os.name == "posix":
        os.system("clear")

    else:
        os.system("cls")


def login():
    pass_count = 0
    err_count = 0
    a = 1
    while a == 1:
        USERNAME = input("ENTER USERNAME: ")
        PASSWORD = input("ENTER PASSWORD: ")
        check = [USERNAME, PASSWORD]
        query = "select username,password from users where username='{}'".format(
            USERNAME.lower())
        mycursor.execute(query)
        res = mycursor.fetchall()
        list = []
        if res != []:
            for i in res:
                for j in i:
                    list.append(j)
            if list == check:
                print("\n", "="*8, "LOGIN SUCCESSFULL", "="*8, "\n")
                time.sleep(4)
                main()
                a = 2
            else:
                print("\n", "="*8, "incorrect password", "="*8, "\n")
                pass_count += 1
                if pass_count > 2:
                    print("CONTACT THE ADMINISTRATOR TEAM FOR RESETTING YOUR PASSWORD")
                    break
                else:
                    time.sleep(2)

        else:
            print("\n", "="*8, "INVALID USERNAME", "="*8, "\n")
            err_count += 1
            if err_count > 2:
                print("CONTACT THE ADMINISTRATION TEAM")
                break
            else:
                time.sleep(2)


def main():
    heading()
    print("\n", "="*8, "MAIN MENU", "="*8, "\n")

    print("OPTION 1: ADMISSION MENU")
    print("OPTION 2: STUDENT DATA")
    print("OPTION 3: FEES DETAILS")
    print("OPTION 4: STAFF DETAILS")
    list = [str(i) for i in range(1, 5)]

    while True:
        response = input("\nENTER OPTION NUMBER: ")
        if response not in list:
            print("\n", "="*8, "ENTER A VALID OPTION", "="*8, "\n")

        elif response == list[0]:
            ADMMISSION_MENU()
            break
        elif response == list[1]:
            STUDENT_DATA()
            break
        elif response == list[2]:
            FEES_DETAILS()
            break
        elif response == list[3]:
            STAFF_DETAILS
            break


def ADMMISSION_MENU():
    print("\n", "="*8, "ADMISSION_MENU", "="*8, "\n")

    print("OPTION 1: ADD STUDENT")
    print("OPTION 2: DEL STUDENT")
    print("OPTION 3: SHOW STUDENTS")
    options = [str(i) for i in range(1, 4)]

    def add_student():
        rollno = random.randint(10000, 99999)
        NAME=input("ENTER NAME OF STUDENT: ")
        SEX=input("ENTER SEX OF THE STUDENT (M/F): ")
        PHONE_NO=input("ENTER PHONE NUMBER OF PARENT: ")
        EMAIL_ID=input("ENTER EMAIL ID OF PARENT: ")
        DOB=i
        pass

    def del_student():
        pass

    def show_students():
        pass

    while True:
        response = input("\n ENTER OPTION NUMBERS: ")
        if response not in options or response == "" or response.isspace():
            print("\n", "="*8, "ENTER VALID OPTION", "="*8, "\n")
        elif response == options[0]:
            add_student()
            break
        elif response == options[1]:
            del_student()
            break
        elif response == options[2]:
            show_students()
            break


def STUDENT_DATA():
    pass


def FEES_DETAILS():
    pass


def STAFF_DETAILS():
    pass


if __name__ == "__main__":
    ADMMISSION_MENU()
