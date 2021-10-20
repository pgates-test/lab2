#konwersja km na mile i odwrotnie
def mile():
    a=int(input("podaj predkosc w mph:"))
    t = a*1.609344
    print("predkosc w kmh: ")
    print(t)
def km():
    a=int(input("podaj predkosc w kmh:"))
    t = a*0.6214
    print("predkosc w mph: ")
    print(t)

x=int(input("podaj w czym(1-mph/kmh /2-kmh/mph)"))

if x == 1:
    km()
elif x == 2:
    mile()