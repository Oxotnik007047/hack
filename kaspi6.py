import time
import os
import sys
from time import sleep
def soz():
    print ("1.vaxt\n2.Kalkulator")
    komand=input("-")
    if komand=="1":
        print(time.asctime())
        soz2()
    if komand=="2":
        kal()
    else:
        soz2()
def soz2():
    print("1.Davam et\n2.Davam etmə")
    a=input("-")
    if a=="1":
        soz()
    elif a=="2":
        sys.exit()
    else:
        print("Mən səni anlamıram")
        soz2()    
def kal():
    print("Birinci ədəd:")
    bir=float(input("-"))
    print("Işarə:")
    ish=input("-")
    print ("Ikinci ədəd")
    iki=float(input("-"))
    cav=bir+iki
    cav2=bir-iki
    cav3=bir*iki
    cav4=bir/iki
    if ish=="+":
        print("Cavab:"+ str(cav))
    elif ish=="-":
        print("Cavab:"+ str(cav2))
    elif ish=="*":
        print("Cavab:"+ str(cav3))
    elif ish=="/":
        print("Cavab:"+ str(cav4))
    else:
        print("Mən səni anlamıram")
        soz2()
    soz2()
soz()
