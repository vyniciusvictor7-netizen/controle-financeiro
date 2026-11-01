from datetime import datetime
data = "2026-12-25 18:30:00"
data_objeto = datetime.strptime(data,"%Y-%m-%d %H:%M:%S")
print(type(data_objeto))
print(data_objeto)

mostrar_data = data_objeto.strftime("%d/%m/%Y %H:%M" )
print(mostrar_data)