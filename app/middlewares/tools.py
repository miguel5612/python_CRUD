def keyValueFromArreglo(arreglo):
    concatenado = ''
    contador = 0
    for key,value in arreglo.items():
        concatenado += "'" + key + "'" + "='" + value + "'"
        contador+=1
        if(contador<len(arreglo)): concatenado += ','
    return concatenado
def keyValueFromArregloWithAph(arreglo):
    concatenado = ['', '']
    contador = 0
    for key,value in arreglo.items():
        concatenado[0] += "'" + key + "'" 
        concatenado[1] += "'" + value + "'"
        if(contador<len(arreglo) - 1): 
            concatenado[0] += ','
            concatenado[1] += ','
            contador+=1
    return concatenado
def keyValueFromArregloWithAnd(arreglo):
    concatenado = ''
    contador = 0
    for key,value in arreglo.items():
        concatenado += key + "='" + value + "'"
        contador+=1
        if(contador<len(arreglo)): concatenado += ' AND '
    return concatenado
def proxy2obj(proxy):
    d, a = {}, []
    for rowproxy in proxy:
        # rowproxy.items() returns an array like [(key0, value0), (key1, value1)]
        for column, value in rowproxy.items():
            # build up the dictionary
            d = {**d, **{column: value}}
        a.append(d)
    return a