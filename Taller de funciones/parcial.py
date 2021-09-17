def main():
       caso1=["¡LaVidaEsDura!","tijeras papel","papel piedra","piedra lagarto",
              "lagarto Holk","Holk tijeras","tijeras lagarto","lagarto papel",
              "papel Holk","Holk piedra","piedra tijeras"]
       
       caso2=["¡siempre hay un próximo semestre!","papel tijeras","papel piedra","lagarto piedra",
              "Holk lagarto","tijeras Holk","lagarto tijeras","papel lagarto",
              "Holk papel","piedra Holk","tijeras piedra"]
       
       caso3="¡otra vez!"
       
       t=int(input("casos de prueba >>"))
       print ("1.profesor 2.Brigitte, ejemplo: papel piedra")
       c=0
       for j in range (0,t):
              juego=input("ingrese la jugada>>")
              c=c+1
              if juego in caso1:
                     print ("Caso #",c,":",caso1[0])
              elif juego in caso2:
                     print ("Caso #",c,":",caso2[0])
              else:
                     print ("Caso #",c,":",caso3)
              
              
main()