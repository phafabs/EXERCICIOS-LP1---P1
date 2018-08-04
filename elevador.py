pessoa = 1
peso_total = 0 
peso_limite = 560 
max_pessoas = 7
while (pessoa <= 7) and (peso_total <= peso_limite):	
	print("Passageiro: ",pessoa)
	peso_pessoa = float(input("Digite o peso do passageiro: "))
	peso_total += peso_pessoa
	pessoa += 1
if (pessoa >= max_pessoas):
	print("Atingiu o limite máximo de pessoas!", pessoa - 1)
elif (pessoa < max_pessoas) and (peso_total >= peso_limite):
	print("Atingiu o limite máximo de peso, que é: {:.2f} ".format(peso_limite))
	print("Total do peso dos passageiros atuais: {:.2f} ".format(peso_total))
	print("Diminua: {:.2f} ".format(peso_total - peso_limite))
