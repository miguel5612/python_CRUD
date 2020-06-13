import tools
#///////////////////////////////////////////////////////////////////////////////////////////////////////
class Crud:    
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def __init__(self, entidad):
        self.entidad = entidad
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def created(self, data):
        sql = "INSERT INTO %s SET ?" %  self.entidad
        print(sql)
        #resultado  =  await consulta(sql,data)
        #if(!resultado)return false
        #if(resultado.insertId  > 0)return resultado.insertId  
        #else if(resultado.affectedRows > 0)return resultado.affectedRows 
        #else return true
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def index(self):
        sql = "SELECT * FROM %s" % self.entidad
        print(sql)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return resultado
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def read(self, obj):
        sql = "SELECT * FROM {entidad} WHERE {data}".format(entidad = self.entidad, data = tools.keyValueFromArregloWithAnd(obj))
        print(sql)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return resultado
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def update(self, data,key = {'id':0}):
        sql = "UPDATE {entidad} SET {data} WHERE {key} = {value}".format(entidad = self.entidad, data = tools.keyValueFromArreglo(data), key = list(key.keys())[0], value = key[list(key.keys())[0]])
        print(sql)
        #resultado  =  await consulta(sql,data)
        #if(resultado === false)return false
        #return resultado.affectedRows
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    def delete(self, obj):
        sql = "DELETE FROM {entidad} WHERE {key} = '{value}'".format(entidad = self.entidad, key = list(obj.keys())[0], value = obj[list(obj.keys())[0]])
        print(sql)
        #resultado  =  await consulta(sql)
        #if(resultado === false)return false
        #return true 
    #///////////////////////////////////////////////////////////////////////////////////////////////////////
    #///////////////////////////////////////////////////////////////////////////////////////////////////////