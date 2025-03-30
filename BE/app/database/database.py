from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Tải biến môi trường từ file .env
load_dotenv()

# Lấy chuỗi kết nối từ biến môi trường, hoặc sử dụng giá trị mặc định
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:12345678@localhost:5432/introduction-web-app")

# Tạo engine kết nối đến PostgreSQL
engine = create_engine(DATABASE_URL)

# Tạo sessionmaker để quản lý các phiên làm việc với database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class mà tất cả các model sẽ kế thừa
Base = declarative_base()

# Dependency function để tạo và đóng session database
def get_db():
    db = SessionLocal()
    try:
        yield db  # Trả về session cho route handler sử dụng
    finally:
        db.close()  # Đảm bảo session được đóng sau khi xử lý request