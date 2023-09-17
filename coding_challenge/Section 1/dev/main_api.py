from fastapi import FastAPI
import  functions.s3_fun as sf
import  functions.db_fun as db

app=FastAPI()

@app.get("/insertar-registros")
def insertar(tabla,q_filas=None):
    print('Inicia proceso')
    if tabla is None:
        mensaje='ERROR: NO SE ESPECIFICA TABLA DE DESTINO'
    else:
        if q_filas is None:
            print('RECIBIENDO ARCHIVOS CSV')
            registros=sf.leer_csv_s3(tabla)
            print('ARCHIVOS CSV RECBIDOS')
            print('INSERTANDO ARCHIVOS CSV A TABLA')
            db.insertar_registros(registros,tabla)
            print('DATOS INSERTADOS')
            mensaje='SE INSERTO CORRECTAMENTE LA TABLA {}'.format(tabla.upper())
        else:
            filas=int(q_filas)
            print('RECIBIENDO ARCHIVOS CSV')
            registros=sf.leer_csv_s3(tabla)
            print('ARCHIVOS CSV RECBIDOS')
            print('INSERTANDO ARCHIVOS CSV A TABLA')
            db.insertar_registros(registros,tabla,filas)
            print('DATOS INSERTADOS')
            mensaje='SE INSERTO CORRECTAMENTE LA TABLA {} CON {} REGISTROS'.format(tabla.upper(),q_filas)

    
    return {mensaje}