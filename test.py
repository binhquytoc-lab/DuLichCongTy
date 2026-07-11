from database import get_connection

conn = get_connection()

print("Kết nối thành công!")

conn.close()
