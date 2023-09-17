from credentials.db_configuration import config
import pandas as pd
import psycopg2
import psycopg2.extras


def conectar_db():
    try:
        connection = psycopg2.connect(
            user=config.get('db_user'),
            password=config.get('db_pass'),
            host=config.get('db_host'),
            port=config.get('db_port'),
            database=config.get('db_name'),
        )
        cursor = connection.cursor()
        print("Connected to the database successfully")
        return cursor,connection
        
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


def insertar_registros(datos,tabla,n_filas=3000):
    cur,conn=conectar_db()

    ##LIMPIEZA DE DATOS
    if tabla=='departments':
        datos_limpio=(datos[datos['id'].notna() & datos['department'].notna()]).head(n_filas)
    
    if tabla=='employees':
        tabla='hired_employees'
        datos_limpio=(datos[datos['job_id'].notna() & datos['department_id'].notna() & datos['nombre'].notna() & datos['fecha_contrato'].notna()]).head(n_filas)

    if tabla=='jobs':
        datos_limpio=(datos[datos['id'].notna() & datos['job'].notna()]).head(n_filas)

    ##INSERTAMOS LOS DATOS LIMPIOS
    try:
        df_columns=list(datos_limpio)
        columns=",".join(df_columns)
        values="VALUES ({})".format(",".join(["%s" for _ in df_columns]))
        insert_stmt="INSERT INTO {} ({}) {}".format(tabla,columns,values)
        cur.execute("TRUNCATE TABLE " + tabla + ";")
        cur.execute("SET SESSION TIME ZONE 'America/Lima'")
        psycopg2.extras.execute_batch(cur,insert_stmt,datos_limpio.values)
        conn.commit()
        print('REGISTROS INSERTADOS CORRECTAMENTE')
        conn.close()
        print('CERRANDO CONEXION')
    except:
        print('ERROR AL INSERTAR LOS REGISTROS')