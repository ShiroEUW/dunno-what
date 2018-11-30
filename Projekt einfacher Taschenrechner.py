***Fett Kursiv***

x = int(input("Erste Zahl: "))

y = int(input("Zweite Zahl: "))

z = input("Welches Rechnenzeichen möchten Sie verwenden: ")

if z == "+":
    
    print("Das Ergebnis aus", int(x), " + ", int(y))
    print("ist gleich", int(x) + int(y), "!")
    
elif z == "-":
    
    print("Das Ergebnis aus", int(x), " - ", int(y))
    print("ist gleich", int(x) - int(y), "!")
    
    
elif z == "/":
    
    print("Das Ergebnis aus", int(x), " / ", int(y))
    print("ist gleich", int(x) / int(y), "!")
    
elif z == "*":
    
    print("Das Ergebnis aus", int(x), " * ", int(y))
    print("ist gleich", int(x) * int(y), "!")
    
else:
    print(z, "kenne ich nicht")

