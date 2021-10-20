#konwersja c na f i odwrotnie
#c=(f-32)*5/9
#f=(c*9/5)+32
def fahrenhiet():
    a=int(input("podaj temperature w °C:"))
    t = (a*9/5)+32
    print("temperatura w fahrenheitach: ")
    print(t)
def celsius():
    a=int(input("podaj temperature w °F:"))
    t = (a-32)*5/9
    print("temperatura w celsiuszach: ")
    print(t)

x=int(input("podaj w czym(1-Fahrenheit/2-Celsius)"))

if x == 1:
    celsius()
elif x == 2:
    fahrenhiet()
