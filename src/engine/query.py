from DataAccess.connect_database import conn_sql
from Common.get_data_json import get_config
from Utils.utils import util

def main():
    path_out = 'D:\\Dev\\PyDevToolsSQL\\Files\\OUT\\'   
    lista_paises = util.get_value_json(get_config.get_json('countries'))
    suffix = util.get_value_json(get_config.get_json('suffix'))
    sp = input("Ingrese el objeto de base de datos: ")
    archivo_out = open("{}{}.sql".format(path_out,sp),'w+')
    # Read by row result sql 
    # ========================
    query_line = from_sql(sp)
    for pais in lista_paises:    
        archivo_out.write('USE Belcorp{}_{} \n'.format(pais,suffix[0]))
        archivo_out.write('GO \n')
        for line in query_line:
            archivo_out.write(line)
        archivo_out.write('\n')
        archivo_out.write('GO \n\n')      
    archivo_out.close()

    # Read by string result sql 
    # ========================
    # result =  from_sql_v2(sp)
    # for pais in lista_paises:    
    #     archivo_out.write('USE Belcorp{}_{} \n'.format(pais,suffix[0]))
    #     archivo_out.write('GO \n')       
    #     archivo_out.write(result)
    #     archivo_out.write('\n')
    #     archivo_out.write('GO \n\n')      
    # archivo_out.close()


def from_sql(sp):
    query_line = []
    str_cnx_sql = util.get_value_json(get_config.get_json('credentials_database'))
    sql_access = conn_sql(str_cnx_sql[0],str_cnx_sql[1],str_cnx_sql[2],str_cnx_sql[3])
    conn = sql_access.connect()
    query = 'sp_helptext {}'.format(sp)
    cursor = conn.cursor()
    cursor.execute(query)
    row = cursor.fetchone() 
    while row:  
     query_line.append(row[0].rstrip()+'\n')
     row = cursor.fetchone()
    return query_line

def from_sql_v2(sp):
     query_line = ""
     str_cnx_sql = util.get_value_json(get_config.get_json('credentials_database'))
     sql_access = conn_sql(str_cnx_sql[0],str_cnx_sql[1],str_cnx_sql[2],str_cnx_sql[3])
     conn = sql_access.connect()
     query = "select replace(definition, 'CREATE PROCEDURE', 'ALTER PROCEDURE') from sys.sql_modules m join sys.procedures p on m.object_id = p.object_id where name = '{}'".format(sp)     
     cursor = conn.cursor()
     cursor.execute(query)
     row = cursor.fetchone() 
     while row:  
      query_line = row[0].rstrip()
      row = cursor.fetchone()
     return query_line
if __name__ == "__main__":
    main()









    

