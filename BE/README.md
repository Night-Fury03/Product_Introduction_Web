# FastAPI Project

## Giới thiệu

Đây là một dự án FastAPI đơn giản. Hướng dẫn này giúp bạn thiết lập và chạy ứng dụng trên môi trường local.

## Yêu cầu

Trước khi bắt đầu, hãy đảm bảo bạn đã cài đặt:

- Python (>= 3.8)
- Git

## Cách chạy dự án trên local

### 1. Clone dự án

Mở terminal/cmd và chạy:

```bash
git clone https://github.com/Night-Fury03/Product_Introduction_Web
cd BE
```

### 2. Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
source venv/bin/activate  # (Linux/macOS)
venv\Scripts\activate  # (Windows)
```

### 3. Cài đặt dependencies

```bash
pip install -r requirements.txt
```

### 4. Chạy ứng dụng

```bash
uvicorn main:app --reload
```

Ứng dụng sẽ chạy tại: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Môi trường cấu hình

Sử dụng file `.env` để lưu các biến môi trường nếu cần.

## Đóng góp

Nếu bạn muốn đóng góp, hãy fork repository và tạo pull request. 🚀
