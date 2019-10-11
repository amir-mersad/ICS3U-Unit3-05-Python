#!/usr/bin/env python3

# Created by Amir Mersad
# Created on September 2019
# This program gives the month of each number


def main():
    # This function gives the month of each number

    # Input
    number_user = int(input("Please enter the number of month(1-12): "))

    # Process & Output
    if number_user == 1:
        print("January")
    elif number_user == 2:
        print("February")
    elif number_user == 3:
        print("March")
    elif number_user == 4:
        print("April")
    elif number_user == 5:
        print("May")
    elif number_user == 6:
        print("June")
    elif number_user == 7:
        print("July")
    elif number_user == 8:
        print("August")
    elif number_user == 9:
        print("September")
    elif number_user == 10:
        print("October")
    elif number_user == 11:
        print("November")
    elif number_user == 12:
        print("December")
    else:
        print("Wrong input!!!")


if __name__ == "__main__":
    main()
