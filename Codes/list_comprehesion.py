# create a list

number_pow_2 = [i**2 for i in range(10)]
print(f"Resultado: {number_pow_2}")

number_pow_2_pair = [i**2 for i in range(10) if (i**2) % 2 == 0]
print(f"Resultado: {number_pow_2_pair}")

number_pow_2_pair_up_20 = [
    i**2 for i in range(10) if (i**2) % 2 == 0 if (i**2) > 20]
print(f"Resultado: {number_pow_2_pair_up_20}")
