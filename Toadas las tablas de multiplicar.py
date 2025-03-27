import os 
import time #tiempo
a=1
while a <= 10:
    print(f"TABLA DE {a}")
    y=1
    while y <= 10:
        r=a*y
        print(f"{a} x {y} = {r}")
        y+=1
    a+=1
    time.sleep(5) #segundos
    os.system("cls")
    print ()
