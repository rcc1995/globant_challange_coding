from credentials.s3_configuration import config,variables
import pandas as pd
import boto3
from io import StringIO

def conectar_s3():

    session=boto3.Session(**config)
    s3=session.client('s3')

    return s3

def leer_csv_s3(archivo):

    s3=conectar_s3()

    bucket=variables.get('repo')
    if archivo=='departments':
        key='inputs/departments/departments.csv'
        cols=['id', 'department']
    
    if archivo=='employees':
        key='inputs/employees/hired_employees.csv'
        cols=['id', 'nombre', 'fecha_contrato', 'department_id', 'job_id']

    if archivo=='jobs':
        key='inputs/jobs/jobs.csv'
        cols=['id', 'job']
    try:
        obj=s3.get_object(Bucket=bucket,Key=key)
        data=obj['Body'].read().decode('utf-8')
        #columns=['id', 'nombre', 'fecha_contrato', 'department_id', 'job_id']
        df=pd.read_csv(StringIO(data),names=cols)

        ##LIMPIAMOS LOS REGISTROS DE NULLS 
        #df_limpio=df[df['job_id'].notna() & df['department_id'].notna() & df['nombre'].notna() & df['fecha_contrato'].notna()]
        
        return df
    except:
        print('Archivo no encontrado')