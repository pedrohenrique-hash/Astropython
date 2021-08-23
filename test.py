from math import ceil, floor
valor = 0;

def porten():
    global valor

    f = float(input("Porcetagem liga a 100% :"))

    g = input("PorcetPara encontra o valor (V) para encontra a porcetagem(P): ")
    
    if (g == 'V'):

        e = float(input("Digite o valor para encontra a Porcentagem: "))

        valor = (e * 100)/(f)

        valor = round(valor)

        print(f"{valor}")
        pass


    if (g == 'P'):

        e = float(input("Digite a Porcentagem para encontra o valor da porcetagem: "))

        valor = (f * e) / (100)

        valor = round(valor)

        print(f"{valor}")

        

    else:
        print("valor não corresponde a: 'P' porcetagem ou 'V' Valor")

        pass



dia_terras = 365.2564

#3  arredondando a dias  na terras (cima, baixo ou decimais )

print(round(dia_terras))

#1 TT arredondando 

TT = ((50*360)/365)

print("O resultado de TT", TT)

print("TT arredondando ",round(TT))

print("TT ",ceil(TT))

print("(TT/50)=(360/365)")

#2 periodo 

periodo =((360 * 780)/(360 + 49))

#2 periodo arrendondado

arredonda = round(periodo)

print("O periodo arredondando ",round(arredonda))

ano = periodo - 365

print(round(ano))

#5 para forma uma ano completp presica de  43 dias para fazer 365

comp_ano = 365

oresto = 43

parte_de_365 = 322

porten()

print(valor)







