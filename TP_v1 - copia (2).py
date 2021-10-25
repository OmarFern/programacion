
ver= ["A","A","B","B"]
JUEGO=[[0] , [1] , [2] , [3] ]
def imprimir():
       
    for i in range(len(JUEGO)):
          salida="".join(str(i) for i  in JUEGO)
          return print(salida)
    


def juego():

    #ver= ["A","A","B","B"]
    print("--------------------------------------------------------")
    #JUEGO=[0 , 1 , 2 , 3 ]
    JUEGO =[[0] ,[1] ,[2], [3]]
    contador=0
    resultado=""
    
    while contador<3:
            
            ###### inicio#############
            print ( "Fichas y Posiciones  :")
            imprimir()
            num1=int(input("1er. Posición: "))
            contador =contador +1
            JUEGO[num1]=ver[num1]
            print(" ".join(str(i) for i  in JUEGO))#A [1] [2] [3]
         
            
            num2=int(input("2da. Posición: "))
                
            JUEGO[num2]=ver[num2]
            print(" ".join(str(i) for i  in JUEGO))#A A [2] [3]
            if ver[num1]==ver[num2]:
                   contador =contador +1
                   print("siiii")
                    ##-----------------------------
                   print ( "Fichas y Posiciones  :")
                    
                   num1=int(input("1er. Posición: "))
                   contador =contador +1
                   JUEGO[num1]=ver[num1]
                   print(" ".join(str(i) for i  in JUEGO))#A [1] [2] [3]
                     
                        
                   num2=int(input("2da. Posición: "))
                            
                   JUEGO[num2]=ver[num2]
                   print(" ".join(str(i) for i  in JUEGO))#A A [2] [3]
                   if ver[num1]==ver[num2]:
                       contador =contador +1
                       print("siiii" )          
            else:
                print("sin suerte :(...")
                juego()
                #num1=int(input("1er. Posición: "))    
           
        
    print("*****ganaste*****")
juego()

"""
Fichas y Posiciones  :
[0][1][2][3]
1er. Posición: 0
A [1] [2] [3]
2da. Posición: 1
A A [2] [3]
siiii


Fichas y Posiciones  :
1er. Posición: 2
A A B [3]
2da. Posición: 3
A A B B
siiii
*****ganaste*****
>>> 
"""

