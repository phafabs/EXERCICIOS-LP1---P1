def  par ( lista ):
    l = []
    
    se  len (lista) >  0 :
        numero = lista.pop ( 0 )
        if numero %  2  ==  0 :
            l.append (numero)
        l = l + par (lista)
    
    retorno l

o =  int ( input ( " " ))
n =  lista ( intervalo (o))
pares =  lista (par (n))

para eu em pares:
  imprimir (i)
