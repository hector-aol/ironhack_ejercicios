numeros = [3, 4, 6, 7, 8, 9, 10]
#'par','divpor3','otro_tipo'
for numero in numeros:
    if numero % 2 == 0:
        print(f"{numero}: par")
    elif numero % 3 == 0:
        print(f"{numero}: divpor3")
    else:
        print(f"{numero}: otro_tipo")

numeros = ('par' if numero%2== 0 else 'dx3' if numero%3==0 else 'otro' for k in numeros)
print(numeros)
