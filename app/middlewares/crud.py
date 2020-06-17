from . import tools
#///////////////////////////////////////////////////////////////////////////////////////////////////////#///////////////////////////////////////////////////////////////////////////////////////////////////////
class Crud:    
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def __init__(self, entidad):
        self.entidad = entidad
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def create(self, data):
        sql = "INSERT INTO {entidad} ({keys}) VALUES ({values})".format(entidad = self.entidad, keys = tools.keyValueFromArregloWithAph(data, False)[0], values = tools.keyValueFromArregloWithAph(data)[1])
        print('Query de insercion: ',  sql)
        result = db.engine.execute(sql)
        print(result)
        #resultado  =  await consulta(sql,data)
        #if(!resultado)return false
        #if(resultado.insertId  > 0)return resultado.insertId  
        #else if(resultado.affectedRows > 0)return resultado.affectedRows 
        #else return true
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def index(self):
        sql = "SELECT * FROM %s" % self.entidad
        print(sql)
        result = db.engine.execute(sql)
        print(result)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return resultado
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def read(self, data):
        sql = "SELECT * FROM {entidad} WHERE {data}".format(entidad = self.entidad, data = tools.keyValueFromArregloWithAnd(data))
        print(sql)
        result = db.engine.execute(sql)
        print(result)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return resultado
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def update(self, data,key = {'id':0}):
        sql = "UPDATE {entidad} SET {data} WHERE {key} = {value}".format(entidad = self.entidad, data = tools.keyValueFromArreglo(data), key = list(key.keys())[0], value = key[list(key.keys())[0]])
        print(sql)
        result = db.engine.execute(sql)
        print(result)
        #resultado  =  await consulta(sql,data)
        #if(resultado === false)return false
        #return resultado.affectedRows
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def delete(self, data):
        sql = "DELETE FROM {entidad} WHERE {key} = '{value}'".format(entidad = self.entidad, key = list(data.keys())[0], value = data[list(data.keys())[0]])
        print(sql)
        result = db.engine.execute(sql)
        print(result)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return true 
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////