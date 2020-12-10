import math
import numpy
from matplotlib import pyplot as plt

tryb_programu = 0

def rzut_pionowy():
    Hlist = []
    Tlist = []
    V = float(input("Podaj prędkość początkową: "))
    g = 9.80
    Hmax = pow(V, 2)/(2*g)

    Tmax = math.sqrt((pow(V, 2)/pow(g, 2))+ (2*Hmax/g)) + (V/g)

    print(Hmax, Tmax)

    for t in numpy.arange(0, Tmax, 0.01):
        h = V*t-((g*pow(t, 2))/2)
        if h < 0:
            break
        Hlist.append(h)
        Tlist.append(t)

    plt.plot(Tlist, Hlist)
    print("Czas trwania lotu: " + str(max(Tlist)) + " Maksymalna wysokość: " + str(Hmax))
    plt.xlabel('Czas')
    plt.ylabel('Wysokość')
    plt.title('Symulacja rzutu pionowego przy prędkości początkowej: ' + str(V))
    plt.show()

def rzut_ukosny():
    print("tu bedzie rzut ukosny")

def rzut_poziomy():
    Zlist = []
    Hlist = []
    V1 = float(input("Podaj prędkość początkową: "))
    H = float(input("Podaj wysokość początkową: "))
    g = 9.80
    Tmax = math.sqrt(2*H/g)
    Zmax = V1*Tmax

    for t in numpy.arange(0, Tmax, 0.01):
        h = H - (g/2)*pow(t, 2)
        z = V1*t
        if h < 0:
            break
        Hlist.append(h)
        Zlist.append(z)
    
    plt.plot(Zlist, Hlist)

    print("Czas trwania lotu: " + str(Tmax) + " Zasięg: " + str(Zmax))
    plt.xlabel('Odległość')
    plt.ylabel('Wysokość')
    plt.title('Symulacja rzutu poziomego przy prędkości początkowej: ' + str(V1))
    plt.show()

print("Program do obliczania rzutów")
while(tryb_programu != '4'):
    print("1 : rzut pionowy w górę")
    print("2 : rzut poziomy")
    print("3 : rzut ukośny")
    print("4 : opuść program")
    print("Podaj tryb pracy programu: ")
    tryb_programu = input()
    if(tryb_programu == '1'):
        rzut_pionowy()
    elif(tryb_programu == '2'):
        rzut_poziomy()
    elif(tryb_programu == '3'):
        rzut_ukosny()
    elif(tryb_programu == '4'):
        print("Koniec pracy programu")
    else:
        print("PODAJ POPRAWNA WARTOSC TRYBU PROGRAMU")
   

    