#!user/bin/env python3

# Created by: RJ Fromm
# Created on: September 2019
# This program is a number guessing game

import constants


def main():

    secret_number = int(input("Guess my secret number : "))

    if secret_number == constants.number:
        print("Good job")


if __name__ == "__main__":
    main()
