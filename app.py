aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
potencia = float(input("Digite a potência do aparelho em Watts (W): "))
horasDia = float(input("Digite o tempo médio de uso diário em horas: "))

consumoMensal = (potencia * horasDia * 30) / 1000
custoEstimado = consumoMensal * 0.75

print(f"\nAparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custoEstimado:.2f} por mês")