def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso. É recomendado procurar um médico para avaliação criteriosa do resultado. Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados."
    elif imc < 25:
        return "Peso normal.  Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal, para compreender se estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da normalidade, mas têm circunferência abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal."
    elif imc < 30:
        return "Sobrepeso. É importante considerar mudanças no estilo de vida, como dieta e atividade física, para evitar complicações à saúde."
    elif imc < 35:
        return "Obesidade grau I. É recomendada a busca por orientação profissional para avaliação e possíveis intervenções."
    elif imc < 40:
        return "Obesidade grau II. É recomendada a busca por orientação profissional para avaliação e possíveis intervenções."
    else:
        return "Obesidade grau III. É recomendada a busca por orientação profissional para avaliação e possíveis intervenções."

# Programa para calcular o IMC e classificar o estado nutricional
try:
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em centímetros: "))
    altura = altura / 100  # Convertendo altura de cm para m
    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"\nSeu IMC é: {imc:.1f}")
    print(f"Classificação: {classificacao}")
except ValueError:
    print("Por favor, insira valores numéricos válidos.")