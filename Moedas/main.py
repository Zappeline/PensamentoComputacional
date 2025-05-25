from models.produtos import produtos

refrigerante = produtos("", 9.80, "BRL")

print(refrigerante)

refrigerante.get_nome() 

print(refrigerante)

refrigerante.set_nome("Guarana")

print(refrigerante)

refrigerante.set_preco(11)

print(refrigerante)


