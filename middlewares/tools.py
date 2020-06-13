def keyValueFromArreglo(arreglo):
    concatenado = ''
    contador = 0
    for key,value in arreglo.items():
        concatenado += "'" + key + "'" + "='" + value + "'"
        contador+=1
        if(contador<len(arreglo)): concatenado += ','
    return concatenado
def keyValueFromArregloWithAnd(arreglo):
    concatenado = ''
    contador = 0
    for key,value in arreglo.items():
        concatenado += "'" + key + "'" + "='" + value + "'"
        contador+=1
        if(contador<len(arreglo)): concatenado += ' AND '
    return concatenado
