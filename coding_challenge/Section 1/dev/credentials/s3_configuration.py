import os 

##SE USA VARIABLES DE ENTORNO PARA NO HARDCODEAR, LO CUAL ES MALA PRACTICA
config = dict(
           aws_access_key_id=os.environ.get('access_key_id'),
           aws_secret_access_key=os.environ.get('secret_access_key'),
           region_name='us-east-1'
        )

variables=dict(

    repo='rcc95-dev-test'
)
