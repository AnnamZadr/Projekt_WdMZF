import math
import numpy
from matplotlib import pyplot as plt

tryb_programu = 0

def rzut_pionowy():
    Hlist = []
    Tlist = []
    V = input("Podaj prędkość początkową: ")
    if V.isnumeric() == False:
        while V.isnumeric() == False:
            print("Podane wcześniej wartości sa niepoprawne, wpisz wartości liczbowe!")
            V = input("Podaj prędkość początkową: ")
    V = float(V)
    g = 9.81
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
    plt.axis('scaled')
    plt.xlabel('Czas')
    plt.ylabel('Wysokość')
    plt.title('Symulacja rzutu pionowego przy prędkości początkowej: ' + str(V)+ 'm/s\n'
    'Czas: '+str(round(Tmax,2)) +'s' +
    ' Maks. Wys.: '+str(round(Hmax,2)) +'m')
    plt.show()

def rzut_ukosny():
    Zlist = []
    Hlist = []
    DtoR = 0.0174533
    V = input("Podaj prędkość początkową: ")
    Kat = input("Podaj kąt pod jakim zostało rzucone ciało: ")
    if V.isnumeric() == False or Kat.isnumeric() == False:
        while V.isnumeric() == False or Kat.isnumeric() == False:
            print("Podane wcześniej wartości sa niepoprawne, wpisz wartości liczbowe!")
            V = input("Podaj prędkość początkową: ")
            Kat = input("Podaj kąt pod jakim zostało rzucone ciało: ")
    V = float(V)
    Kat = float(Kat)
    Kat = Kat*DtoR
    g = 9.81
    Tmax = 2*V*math.sin(Kat)/g
    Zmax = V*Tmax*math.cos(Kat)

    for t in numpy.arange(0, Tmax, 0.01):
        h = (V*t*math.sin(Kat)) - (g/2*pow(t, 2))
        z = V*t*math.cos(Kat)
        Hlist.append(h)
        Zlist.append(z)
    
    plt.plot(Zlist, Hlist)
    plt.axis('scaled')
    plt.xlabel('Odległość')
    plt.ylabel('Wysokość')
    plt.title('Symulacja rzutu ukośnego przy prędkości początkowej: ' + str(V) + 'm/s\n'
    'Zasięg: '+str(round(Zmax,2))+'m' +
    ' Czas: '+str(round(Tmax,2))+'s' +
    ' Maks. Wys.: '+str(round(max(Hlist),2))+'m' +
    ' Kat: '+str(round(Kat/DtoR,2))+'°')
    plt.show()

def rzut_poziomy():
    Zlist = []
    Hlist = []
    V1 = "predkosc"
    H = "wysokosc"
    V1 = input("Podaj prędkość początkową: ")
    H = input("Podaj wysokość początkową: ")
    if H.isnumeric() == False or V1.isnumeric() == False:
        while H.isnumeric() == False or V1.isnumeric() == False:
            print("Podane wcześniej wartości sa niepoprawne, wpisz wartości liczbowe!")
            V1 = input("Podaj prędkość początkową: ")
            H = input("Podaj wysokość początkową: ")
    V1 = float(V1)
    H = float(H)
    g = 9.81
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
    plt.axis('scaled')
    plt.xlabel('Odległość')
    plt.ylabel('Wysokość')
    plt.title('Symulacja rzutu poziomego przy prędkości początkowej: ' + str(V1) + 'm/s\n'
    'Zasieg:'+str(round(Zmax,2)) +'m' + 
    ' Czas: '+str(round(Tmax,2)) +'s' +
    ' Maks. Wys.: '+str(round(H,2)) +'m')
    print('Zamknij okno z symulacją, aby kontynuować  ...')
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
   

    