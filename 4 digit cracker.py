import keyboard
import time

#Create Passwords
p_p = []

for i in range(0, 10000):
    if i < 10:
        p_p.append("000{}".format(i))
    elif i < 100:
        p_p.append("00{}".format(i))
    elif i < 1000:
        p_p.append("0{}".format(i))
    else:
        p_p.append(str(i))

#Entering the password
for i in p_p:
    for x in i:
        keyboard.write(x)
