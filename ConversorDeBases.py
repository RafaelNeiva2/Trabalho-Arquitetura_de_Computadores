import sys

def conversorBinarioDecimal(binario):
    binario = list(binario)
    decimal = 0
    for i in range(len(binario)):
        decimal += int(binario[i])*2**(len(binario) - i - 1)

    return decimal

def conversorBinarioDecimalSM(binario):
    if binario[0] == '0':
        sinal = 1
    else:
        sinal = -1

    magnitude = int(binario[1:], 2)

    decimal = sinal * magnitude

    return decimal

result = ''
def somaBin(b1,b2):
    result = ''
    carry = 0
    i = len(b1) - 1
    j = len(b2) - 1

    while i >= 0 or j >= 0 or carry:
        total = carry
        if i >= 0:
            total += int(b1[i])
            i -= 1
        if j >= 0:
            total += int(b2[j])
            j -= 1
        result = str(total % 2) + result
        carry = total // 2

    return result.zfill(32)



def subBin(b1,b2):
    result = ''
    emprestimo = 0
    i = len(b1) - 1
    j = len(b2) - 1

    while j>=0 or i>=0 or emprestimo!=0:
        if i >= 0:
            x = int(b1[i])
        else:
            x=0
        if j >= 0:
            y= int(b2[j])
        else:
            y=0

        dif = x - y - emprestimo

        if dif < 0:
            dif = dif + 2
            emprestimo = 1
        else:
            emprestimo = 0

        result = str(dif) + result
        i -= 1
        j -= 1

    if emprestimo == 1:
        result = '-' + result
    else:
        result = result

    return result.zfill(32)

def convertor_c2(num_bin):
    lista_c2 = list(num_bin)

    for i in range(len(lista_c2)):
        if lista_c2[i] == '0':
            lista_c2[i] = '1'
        else:
            lista_c2[i] = '0'

    auxiliar = 1
    for i in range(len(lista_c2)-1, -1, -1):
        if auxiliar == 0:
            break
        elif lista_c2[i] == '0':
            lista_c2[i] = '1'
            auxiliar = 0
        else:
            lista_c2[i] = '0'

    return ''.join(lista_c2)

def conversor_c2_decimal(binario):

    binario = list(binario)

    if binario[0] == '1':
        b1 = -(conversorBinarioDecimal(convertor_c2(binario)))
    else:
        b1 = conversorBinarioDecimal(binario)

    return b1

#arquivotxt
with open(sys.argv[1],"r" ) as i:
    b1,b2 = i.read().split("\n")

#formatacao de respostas
#printa os numeros de SM na base 10
print(conversorBinarioDecimalSM(b1))
print(conversorBinarioDecimalSM(b2) , "\n")

#printa a soma e subtração dos valores de SM na base 2
print(subBin(b1,b2))
print(somaBin(b1,b2),"\n")

#printa a soma e subtração de Sm na base 10
print(conversorBinarioDecimalSM(subBin(b1,b2)))
print(conversorBinarioDecimalSM(somaBin(b1,b2)),"\n")

#printa os valores de C2 na base 10
print(conversor_c2_decimal(b1))
print(conversor_c2_decimal(b2), "\n")

#printa a soma e subtração de C2 na base 2
print(somaBin(convertor_c2(convertor_c2(b1)),convertor_c2(convertor_c2(b2))))
print(subBin(convertor_c2(convertor_c2(b1)),convertor_c2(convertor_c2(b2))),"\n")

#printa a soma e subtração de C2 na base 10
print(conversor_c2_decimal(somaBin(convertor_c2(convertor_c2(b1)),convertor_c2(convertor_c2(b2)))))
print(conversor_c2_decimal(subBin(convertor_c2(convertor_c2(b1)),convertor_c2(convertor_c2(b2)))))










