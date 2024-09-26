def imc_calculate(height: float, weight: float):
    return weight / height**2

user_height = float(input('Digite sua altura: '))
user_weight = float(input('Digite seu peso: '))

print(f"Seu IMC é: {imc_calculate(height = user_height, weight = user_weight):.2f}")