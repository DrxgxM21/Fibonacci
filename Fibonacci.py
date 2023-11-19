#E
Fibonacci= [1,1]

def Anzahlderstellenabfragen(promt):
    while True:
        try:
            Anzahl = int(input(promt))
            return Anzahl
        except ValueError:
            print('Du Honk wieso bist du so dumm ? ')

Anzahl= Anzahlderstellenabfragen("Nenne mir die Anzahl der Stellen die du vom Fibonacci Code haben willst> ")


#V
def Anzahlderstellenabfragenverarbeitung(Wiederholunge):
    if Wiederholunge <= 0:
        return None
    if Wiederholunge == 1:
        print("test")
        Fibonacci.pop(1)
        return Fibonacci
    if Wiederholunge <= 2:
        return Fibonacci[:Wiederholunge]
    else:
        for Neuenummer in range(Wiederholunge - 2):
            Neuenummer = Fibonacci[-1] + Fibonacci[-2]
            Fibonacci.append(Neuenummer)


Anzahlderstellenabfragenverarbeitung(Anzahl)

#A
print(f' Bei deinen gewünschten stellen sieht der Code folgender maßen aus {Fibonacci}')
