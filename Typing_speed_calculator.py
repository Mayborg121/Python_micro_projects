from time import *
import random as r


def mistake(partest,usertest) :
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i] :
                error = error +1               
        except:
            error = error + 1
    return error
            

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)
     



test =["My name is Mayur Borgude , this is the test program to test your typing speed created by me as a python mini project","Hope is the greatest capital we have",]
test1 = r.choice(test)
print("***** Typing speed calculator *****")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter Your Response : ")
time_2 = time()
print()
print("***** Results *****")
print("Speed : ",speed_time(time_1,time_2,testinput),"words/sec, Error/s : ",mistake(test1,testinput))
