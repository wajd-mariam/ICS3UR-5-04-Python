#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program calculates the volume of the cylinder

import math


def volume(radius, height):
    # this function calculates volume

    # process
    volume = math.pi * (radius*radius) * height

    return volume


def main():
    # calling other functions
    while True:
        # input
        radius_from_user = input("Enter the radius of the cylinder: ")
        height_from_user = input("Enter the height of the cylinder: ")

        # try statement
        try:
            radius_from_user_int = int(radius_from_user)
            height_from_user_int = int(height_from_user)

            if radius_from_user_int < 0 and height_from_user_int < 0:
                print("Not a valid entry")

            else:
                volume_of_cylinder = volume(height=height_from_user_int,
                                            radius=radius_from_user_int)

                print("The volume is {}cm³".format(round(volume_of_cylinder)))

        except (ValueError):
            print("Invalid entry, please try again")


if __name__ == "__main__":
    main()
