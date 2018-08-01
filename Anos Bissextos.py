antigo = int(input('Digite ano antigo: '))
novo = int(input('Digite ano recente: '))
for a in range(antigo, novo):
  if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(a)
