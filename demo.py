import random
import pandas as pd
import psycopg2
from time import sleep

# Đọc file CSV
df = pd.read_csv('employees.csv')

# Chọn ngẫu nhiên một dòng (record)
random_record = df.sample(n=1).iloc[0]

# In thông báo chuẩn bị thêm dữ liệu vào hệ thống
print("Chuẩn bị thêm dữ liệu vào hệ thống")

# Thông tin kết nối tới PostgreSQL (thay đổi nếu cần thiết)
db_config = {
    'dbname': 'your_dbname',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

def insert_data(record):
    try:
        # Kết nối đến cơ sở dữ liệu PostgreSQL
        conn = psycopg2.connect(**db_config)
        cursor = conn.cursor()

        # SQL Query để chèn dữ liệu
        insert_query = """
        INSERT INTO employees (id, name, age, city, salary)
        VALUES (%s, %s, %s, %s, %s)
        """

        # Thực hiện insert vào bảng
        cursor.execute(insert_query, (record['id'], record['name'], record['age'], record['city'], record['salary']))

        # Commit thay đổi vào cơ sở dữ liệu
        conn.commit()

        # Thông báo thành công
        print("Chèn dữ liệu thành công")
        cursor.close()
        conn.close()

    except psycopg2.IntegrityError as e:
        # Lỗi trùng ID
        print("Đã tồn tại bản ghi trong hệ thống")
        cursor.close()
        conn.close()
        return False
    except Exception as e:
        # Lỗi kết nối cơ sở dữ liệu hoặc lỗi khác
        print(f"Lỗi: {str(e)}")
        return False

    return True

# Thử 3 lần nếu trùng ID
attempts = 0
success = False
while attempts < 3 and not success:
    success = insert_data(random_record)
    if not success:
        attempts += 1
        print(f"Thử lại lần {attempts} sau 3 phút...")
        sleep(180)  # Chờ 3 phút (180 giây)

# In ra thông báo hoàn thành
print("Hoàn thành việc chèn dữ liệu")



