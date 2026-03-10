#faccio una funzione "disegna quadrato" e "disegna triangolo": scrivo informazioni per disegnare triangolo e quadrato in modo pù rapido


import turtle

'''
def disegna_quadrato(tartaruga, size, angolo):  #aggiungo una dimensione
   for i in range(4):
     tartaruga.forward(size)   #tartaruga.forward(50)
     tartaruga.left(angolo)


def somma(a,b): 
  risultato = a + b 
  return risultato
  #posso scrivere solo : return = a + b
##################################

result = somma(3,44)
print(result)                  #guardo sotto il disegno e mi restituisce il risultato
#print(a)                       #non ho definito a perchè esiste solo nella funzione somma 
     
#costruisco la finestra di lavoro con le sue proprietà:
window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello: definisco la mia tartaruga
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)
                  # con raffaello

disegna_quadrato(raffaello, 50, 90)

raffaello.right(180)                   # giro e sposto dall'origine raffaello
raffaello.forward(80)                  # 


donatello = turtle.Turtle()            # Istanza di Turtle chiamata donatello
donatello.color("violet")          # attributi per lo stato di donatello
donatello.pensize(4)

def disegna_triangolo(tartaruga, size):
  for i in range(3):
    tartaruga.forward(size)
    tartaruga.left(120)


          

disegna_quadrato(donatello,100, 90)

disegna_triangolo(donatello,70)

window.mainloop()                      # Attendo chiusura finestra di gioco o stop del programma
'''

def koch(t, order, size):
    """
       La tartaruga t disegna frattale Koch di 'order' and 'size'
       lasciando la tartaruga nella direzioni iniziale
    """

    if order == 0:          
        # caso base che termina la ricorsione
        t.forward(size)
    else:
        # caso ricorsivo (ordine 1) in cui disegna i 4 segmenti
        koch(t, order-1, size/3)  
        t.left(60)
        koch(t, order-1, size/3)
        t.right(120)
        koch(t, order-1, size/3)
        t.left(60)
        koch(t, order-1, size/3)
        ##
        
window = turtle.Screen()               # istanza "window" di Screen
window.bgcolor("lightgreen")           # imposto lo stato della "window"
# window.title("Raffaello & Donatello")

raffaello = turtle.Turtle()            # Istanza di Turtle chiamata raffaello: definisco la mia tartaruga
raffaello.color("red")                 # attributi per lo stato di raffaello    
raffaello.pensize(5)

koch(raffaello, 4, 300)

window.mainloop()