import random
Lista = []



while True:
    Jogar = str(input("Quer jogar um jogo?: "))
    if Jogar == "sim"  or "SIM" or "Sim":
        A = random.randint (1, 6)
        B = random.randint (1, 6)
        Resultado = A+B
        Ponto = False

        if Resultado == 7 and Ponto == False or Resultado == 11:
            print("Ganhamo")
            print(Resultado)
            Lista.append (Resultado)
            print(Lista)
            break
            
        elif Resultado == 7 and Ponto == True or Resultado <= 3 or Resultado == 12:
            print ("Perdeu,")
            print(Resultado)
            Lista.append (Resultado)
            print(Lista)
            break
        
        elif Resultado >= 4 and Resultado <= 10:
            for Resultado in Lista:
                print("Ganhamo")                
                break  
            Lista.append (Resultado)
            print(Lista)
            Ponto = True
            print(Resultado)            
        else:
            print("complications, patrao")
            break
            

