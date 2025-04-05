import csv
from faker import Faker

# Khởi tạo đối tượng Faker
fake = Faker()

# Mở file csv để ghi dữ liệu
with open('employees.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Ghi header
    writer.writerow(['id', 'name', 'age', 'city', 'salary'])
    
    # Tạo và ghi 10 records dữ liệu giả
    for i in range(10):
        id = i + 1
        name = fake.name()
        age = fake.random_int(min=20, max=60)
        city = fake.city()
        salary = fake.random_number(digits=5)
        
        writer.writerow([id, name, age, city, salary])

print("Dữ liệu đã được ghi vào file employees.csv")
