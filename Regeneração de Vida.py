vida =  100
regen =  0
tempo = []

x =  int ( input ( " " ))

para eu na  faixa (x):
  
  d, t =  input ( " " ) .split ()
  d =  int (d)
  t =  int (t)
  vida = vida - d
  tempo.append (t)

regen =  max (tempo) -  min (andamento)

y =  int ( entrada ( " " ))

regen = regen * y
vida = vida + regeneração

se vida >  0 :
  imprimir ( " Inimigo Vivo " )
else :
  imprimir ( " Inimigo Morto " )
