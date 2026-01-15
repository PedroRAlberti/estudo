numero = 3941
cod_rom = ""
cont_centena = 0
cont_dezena = 0
#estes sao os contadores de cada casa decimal.
# a seguir, os contadores recebem seus respectivos valores
while numero > 999:
    cod_rom+= "M"
    numero -= 1000
while numero > 99:
    cont_centena += 1
    numero -= 100
while numero > 9:
    cont_dezena += 1
    numero -= 10
#agora, basta adicionar as letras referentes a cada casa decimal
if cont_centena == 9:
    cod_rom += "CM"
elif cont_centena == 4:
    cod_rom += "CD"
elif cont_centena >= 5:
    cod_rom += "D" + (cont_centena - 5)*"C"
else:
    cod_rom += cont_centena*"C"
   
if cont_dezena == 9:
    cod_rom += "XC"
elif cont_dezena == 4:
    cod_rom += "XL"
elif cont_dezena >= 5:
    cod_rom += "L" + (cont_dezena - 5)*"X"
else:
    cod_rom += cont_dezena*"X"
#e a casa das unidades também é o próprio número após aquele processo
if numero == 9:
    cod_rom += "IX"
elif numero == 4:
    cod_rom += "IV"
elif numero >= 5:
    cod_rom += "V" + (numero - 5)*"I"
else:
    cod_rom += numero*"I"
print(cod_rom)