testo = '''
Day after day, day after day,             
We stuck, nor breath nor motion;
As idle as a painted ship
Upon a painted ocean.

Water, water, every where,
And all the boards did shrink;
Water, water, every where,
Nor any drop to drink.

The very deep did rot: O Christ!
That ever this should be!
Yea, slimy things did crawl with legs
Upon the slimy sea.

About, about, in reel and rout
The death-fires danced at night;
The water, like a witch's oils,
Burnt green, and blue and white.
'''

#risolvendo parte 1 esercizio 2

#divido il testo in base al carattere \n
lista_righe = testo.split('\n')            #dividiamo il testo in tutte le volte in cui va a capo

contatore = 0
for riga in lista_righe: 
    if len(riga) > 0: 
        contatore = contatore + 1
    
print(contatore)                           #conto tutte le righe

'''
lista_parole = testo.split(' ')
print(lista_parole)                        #ora le parole sono unite dai caratteri speciali: voglio torgliere i caratteri speciali e togliere gli spazi
'''
lista_parole = testo.split()
print(lista_parole)
contatore = 0
for parola in lista_parole: 
    if len(parola) > 0: 
        contatore = contatore + 1
    
print(contatore)


#punto 8
n = 0, 1, 2, 3
for riga in lista_righe 
    if riga in [1 + 4 * n]


for indice in [1, 5, 9, 13]
    if 