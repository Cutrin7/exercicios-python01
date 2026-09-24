capital = float(input("Quanto você deseja investir? "))
taxa = float(input("Qual a taxa? "))
tempo = float(input("Quanto tempo você deseja investir? "))

montante = capital * (1 + taxa/100) ** tempo

print(f"O valor final do investimento foi de {montante: .2f}")
