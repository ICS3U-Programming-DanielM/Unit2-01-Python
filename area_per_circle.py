#!/usr/bin/env python3

# Created by: Daniel Momoh
# Created on: Sept. 21, 2022
# This program calculates and displays the area and perimeter of a circle with radius 25cm.
import math

def main():
    print ("For a circle that has a radius")
    print ("of 25cm:")
    print ("")
    print ("Area = {} cm^2". format (math.pi*25**2))
    print ("Perimeter = {} cm". format (2*math.pi*25))


if __name__ == "__main__":
  main()