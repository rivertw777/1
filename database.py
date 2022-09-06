from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#이용자 db 테이블
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(32))
    user_pw = db.Column(db.String(32))
    mileage = db.Column(db.String(32))
    serial_num = db.Column(db.String(32))
#유저 아이디, 비밀번호, 마일리지(커피박 수거량), 시리얼넘버로 칼럼 구성

#수거함 db 테이블
class Box(db.Model):
    __tablename__ = 'Box'
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String(32))
    long = db.Column(db.String(32))
    box_id = db.Column(db.String(32))
    grade = db.Column(db.String(32))
#수거함 위도, 경도, 이름, 포화도로 칼럼 구성