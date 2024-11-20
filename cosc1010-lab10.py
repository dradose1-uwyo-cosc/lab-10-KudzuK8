# Nelia Koontz
# UWYO COSC 1010
# Submission Date 11/20/24
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: 
# google search "what is a hash"
# Python Crash Course, especially chapter 10
# Emmanuel and I looked at the code for homework 4 to remember how I read a file
# and split the lines

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."
path = Path('hash')
# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

path_1 = Path('rockyou.txt')

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.
try:
    hash_line = path.read_text()
    rock_you = path_1.read_text()
    ry_lines = rock_you.splitlines()
    for line in ry_lines:
        ry_out = get_hash(line)
        if ry_out == hash_line:
            print(line)
            break
except:
    print("any error")


# - Read in the value stored within `hash`.
#   - You must use a try and except block.


# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
