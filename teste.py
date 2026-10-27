from datetime import datetime

data = datetime.now()

data_formatada = data.strftime('%Y-%m-%d')
hora_formatada = data.strftime('%H:%M:%S')
print(data_formatada, hora_formatada)
