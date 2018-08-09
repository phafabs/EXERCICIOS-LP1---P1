a = int(input('Valor 1:'))
b = int(input('Valor 2:'))
i = 1
cont = 0
cont2 = 0
for i in range(1, 50 + 1):
  if a % i == 0:
        cont = cont + 1
  if b % i == 0:
        cont2 = cont2 + 1
  i = i + 1
print(cont + cont2)
