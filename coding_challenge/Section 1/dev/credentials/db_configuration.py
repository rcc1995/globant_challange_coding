import os 

##SE USA VARIABLES DE ENTORNO PARA NO HARDCODEAR, LO CUAL ES MALA PRACTICA
config = dict(
           db_user=os.environ.get('db_user'),
           db_pass=os.environ.get('db_pass'),
           db_host=os.environ.get('db_host'),
           db_port=os.environ.get('db_port'),
           db_name=os.environ.get('db_name')
        )
