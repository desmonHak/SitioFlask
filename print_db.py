import sqlite3

from consultas_sql import *

try:
    bd = sqlite3.connect(name_data_db)
    cursor = bd.cursor()
    sentencia = select_all.format("users")
 
    cursor.execute(sentencia)
    
    users = cursor.fetchall()
    print("+{:-<20}+{:-<20}+{:-<30}+".format("", "", "", ""))
    print("|{:^20}|{:^20}|{:^30}|".format("user", "password", "fecha_creacion"))
    print("+{:-<20}+{:-<20}+{:-<30}+".format("", "", "", ""))
 
    for user, password, fecha_creacion in users:
        print("|{:^20}|{:^20}|{:^30}|".format(user, password, fecha_creacion))
    
 
    print("+{:-<20}+{:-<20}+{:-<30}+".format("", "", "", ""))
except sqlite3.OperationalError as error:
    print("Error al abrir:", error)