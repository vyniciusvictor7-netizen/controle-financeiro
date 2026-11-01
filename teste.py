from datetime import datetime

data_str = "05/07/2024"
data = datetime.strptime(data_str, "%d/%m/%Y")
print(data)