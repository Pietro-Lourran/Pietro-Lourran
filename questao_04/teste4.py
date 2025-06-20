
# Autor : Pietro Marchetti

# Lista que guarda os funcionários
funcionarios = []

# três trabalhadores assalariados
a1 = TrabalhadorAssalariado("Pedro", "12345678900")
a1.definir_salario(3000)
funcionarios.append(a1)

a2 = TrabalhadorAssalariado("Julia", "23456789011")
a2.definir_salario(4200)
funcionarios.append(a2)

a3 = TrabalhadorAssalariado("Rafael", "34567890122")
a3.definir_salario(3800)
funcionarios.append(a3)

# três trabalhadores horistas
h1 = TrabalhadorHorista("Lucas", "45678901233")
h1.set_valor_hora(50)
h1.set_horas_mes(160)
h1.calcular_pagamento()
funcionarios.append(h1)

h2 = TrabalhadorHorista("Beatriz", "56789012344")
h2.set_valor_hora(40)
h2.set_horas_mes(150)
h2.calcular_pagamento()
funcionarios.append(h2)

h3 = TrabalhadorHorista("Amanda", "67890123455")
h3.set_valor_hora(60)
h3.set_horas_mes(140)
h3.calcular_pagamento()
funcionarios.append(h3)

# Imprime os pagamentos de todos os funcionários
print("\nPagamentos do mês:\n")
for f in funcionarios:
    print(f"{f.get_nome()}: R$ {f.get_salario():.2f}")
