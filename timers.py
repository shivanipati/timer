
import time

times = int(input("enter the time in second: "))
for i in range(times,0,-1):
    second = i%60
    minutes = int(i/60)%60
    hours = int(i/3600)
    print(f'{hours:02}:{minutes:02}:{second:02}')
    time.sleep(1)
print("Times up !")
