a=int(input("podaj liczbe "))
def funkcja(a):
    i=1
    while i < a-1:
        if a%2==0:
            print("liczba nie jest pierwsza")
            break
        else:
            if i==a%2:
                print("liczba jest pierwsza")

        i+=1

funkcja(a)
