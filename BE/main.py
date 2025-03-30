from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models import ProductModel
from app.schemas import Product

# Khởi tạo ứng dụng FastAPI
app = FastAPI(title="Product API")

# Endpoint lấy tất cả sản phẩm
@app.get("/api/products", response_model=List[Product])
def get_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Lấy danh sách sản phẩm với phân trang.
    - skip: Số sản phẩm bỏ qua
    - limit: Số sản phẩm tối đa trả về
    """
    products = db.query(ProductModel).filter(ProductModel.is_active == True).offset(skip).limit(limit).all()
    return products

# Endpoint lấy sản phẩm theo ID
@app.get("/api/products/{product_id}", response_model=Product)
def get_product(product_id: int, db: Session = Depends(get_db)):
    """
    Lấy thông tin chi tiết của một sản phẩm theo ID.
    Trả về lỗi 404 nếu không tìm thấy sản phẩm.
    """
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Sản phẩm không tồn tại")
    return product

