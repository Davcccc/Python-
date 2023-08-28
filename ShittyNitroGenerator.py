import random
import pyfiglet
import time

ascii_banner = pyfiglet.figlet_format("Made By Dav")
print(ascii_banner)
time.sleep(4)
print("Please dont use this; this is my second day learning python not even sure if it works tbh")



amount = int(input("Amount of codes you want to be generatated "))


uppercase_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_char = uppercase_char.lower()
digits = "0123456789"


upper , lower , dig , srt = True , True , True , True


all = ""

if upper:
    all += uppercase_char 

if lower:
    all += lowercase_char

if dig:
    all += digits


length = 16

for x in range(amount):
    Code = "".join(random.sample(all , length))
    print(Code)