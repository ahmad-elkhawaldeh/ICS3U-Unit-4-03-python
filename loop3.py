#!/usr/bin/env python3

# Created by: Ahmad El-khawaldeh
# Created on: Dec 2020
#  a program that accepts a positive integer;
# then calculates the square (power of 2) of each integer from 0 to this number


def main():

    # input
    positive_integer = print(" Enter how many times to repeat ")
    positive_string = input("Enter Here plz : ")

    # process & output
    try:
        positive_integer = int(positive_string)

        for loop_counter in range(positive_integer + 1):
            positive_exponent = loop_counter ** 2
            print("{0}² = {1}".format(loop_counter, positive_exponent))
    except AssertionError:
        print('Given input is not a number.')
    except ValueError:
        print('Given input is not a number.')


if __name__ == "__main__":
    main()
