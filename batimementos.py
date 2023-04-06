bpm = float(input("Insira seus batimentos por minuto: "))
age = int(input("Qual é a sua idade? "))

if age >= 0 and age <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Seus batimentos estão normais, parabéns!")
    else:
        print("Seus batimentos não estão normais!")

if age >= 8 and age <= 17:
    if bpm >= 80 and bpm <= 100:
        print("Seus batimentos estão normais, parabéns!")
    else:
        print("Seus batimentos não estão normais!")

if age >= 18 and age <= 64:
    if bpm >= 70 and bpm <= 80:
        print("Seus batimentos estão normais, parabéns!")
    else:
        print("Seus batimentos não estão normais!")
 
    if age >= 64:
        if bpm >= 50 and bpm <= 60:
            print("Seus batimentos estão normais, parabéns!")
    else:
        print("Seus batimentos não estão normais!")

if age >= 3 and age <= 7:
    print("Ops... Ainda não temos essa resposta.")