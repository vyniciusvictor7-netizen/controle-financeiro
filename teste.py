from datetime import datetime

data = datetime.now()

data_hora = data.strftime('%Y-%m-%d %H:%M:%S') 
print(data_hora)
