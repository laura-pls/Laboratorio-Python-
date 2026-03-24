import sys

#print('Ciao', sys.argv[1])           #indice 1: es. Pippo è il nome a cui ti dà ciao

#print(sys.argv)
#argv passa le cose in ordine, non ti dice certe info.. 

import argparse 

parser = argparse.ArgumentParser()               # registrare una a una 

parser.add_argument('-n','--nome_esteso', help="E' il nome da stampare")
parser.add_argument('-b','--boolean_value', action='store_true', help="imposta il valore 'True' se trova il parametro")
parser.add_argument('-d','--con_default',  default='riferimento', help="Parametro che ha già un valore di default se non viene fornito l'argomento")
# a differenza di argv per leggere gli argomenti bisogna chiamare la funzione parse_arg

variabili = parser.parse_args()

print(variabili.nome_esteso) 