# Name: decoder.py
# Function: Read in all the key files and decode the secret flag.
# Usage: Execute this decoder under the same directory with all the *.txt files in order to get the secret flag.

import os 
import time

currentProgress = 0
barLength = 50

def UselessAnimation(current, total):
    global currentProgress
    global barLength

    if current / total < currentProgress + 0.1:
        return
    time.sleep(1)
    currentProgress = current / total
    currentBar = int(currentProgress * barLength)
    print("decoding " + "*" * currentBar + "." * (barLength - currentBar) + F" {currentProgress*100:.2f}%")


m = int(input("Input the number of key files: "))
n = int(input("Input the length of the secret flag: "))

print("-------------------------------------")
print("Initializing process...")
time.sleep(1.5)

flag = [0] * n
cnt = 0

for filename in os.listdir(os.getcwd()):
    if not filename.endswith(".txt"):
        continue

    with open(os.path.join(os.getcwd(), filename), 'r') as f:
        nums = [int(x) for x in next(f).split()]
        for i in range(n):
            flag[i] = (flag[i] ^ nums[i])

    cnt += 1
    UselessAnimation(cnt, m)
    if cnt == m:
        break

# <more useless animation>
time.sleep(1)
print("decoding " + "*" * barLength + "100.00%")
time.sleep(0.5)
print("-------------------------------------")
print("Decode complete!\n")
time.sleep(0.5)
# </more useless animation>

for num in flag:
    print(chr(num), end='')
print('')
