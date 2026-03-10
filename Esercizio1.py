def is_pari(n):
    """Ritorna vero se "n" è pari, se no ritorna falso """  #docstring

    risultato = False           # oppure: risultato = True   if n%2 != = risultato = False

    if n%2 == 0 : 
        risultato = True 

    return risultato

######

main()
    numero = int( input('Dammi un numero: '))    # creo la funzione input per definire il numero: casting di input all'intero

    print(type(numero))


    result = is_pari(numero)

    print(result)

main()
