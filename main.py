def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso. É recomendado procurar um médico para avaliação criteriosa do resultado. Pode indicar um estado de consumo do organismo, com poucas reservas e riscos associados."
    elif imc < 25:
        return "Peso normal.  Tudo indica que está tudo bem, mas é importante avaliar outros parâmetros da composição corporal, para compreender se estão dentro do recomendado. Algumas pessoas apresentam IMC dentro da normalidade, mas têm circunferência abdominal maior que a recomendada e/ou quantidade de massa gorda acima do ideal."
    elif imc < 30:
        return "Sobrepeso.  O sobrepeso está associado ao risco de doenças como diabetes e hipertensão. Então, atenção! Consulte um médico e reveja hábitos para reverter o quadro. Também é importante avaliar outros parâmetros, como a circunferência abdominal."
    elif imc < 35:
        return "Obesidade grau I. É importante buscar orientação médica e nutricional para entender melhor o seu caso, mesmo que os exames (colesterol e glicemia, por exemplo) estejam normais."
    elif imc < 40:
        return "Obesidade grau II.Indica um quadro de obesidade mais evoluído em relação à classificação anterior e, mesmo com exames laboratoriais dentro da normalidade, não se deve atrasar a busca por orientação médica e nutricional."
    else:
        return "Obesidade grau III. Nesse ponto, a chance de já estarmos diante de outras doenças associadas é mais elevada. É fundamental buscar orientação médica."

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