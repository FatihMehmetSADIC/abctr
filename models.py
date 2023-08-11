from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    TCNo = db.Column(db.String(11), unique=True, nullable=False)
    father_name = db.Column(db.String(100))
    mother_name = db.Column(db.String(100))
    birthplace = db.Column(db.String(100))
    phone_number = db.Column(db.String(20))
    address = db.Column(db.String(255))
    graduation_status = db.Column(db.String(50))
    institution = db.Column(db.String(100))
    field = db.Column(db.String(100))
    dal = db.Column(db.String(100))
    birth_date = db.Column(db.Date)
    
class CompanyInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(255), nullable=False)
    company_address = db.Column(db.String(255), nullable=False)
    company_phone = db.Column(db.String(20), nullable=False)
    company_email = db.Column(db.String(255), nullable=False)
    tax_number = db.Column(db.String(20), nullable=False)
    sgk_registry_number = db.Column(db.String(20), nullable=False)
    sgk_employee_count = db.Column(db.Integer, nullable=False)
    bank_name = db.Column(db.String(255), nullable=False)
    branch_name = db.Column(db.String(255), nullable=False)
    iban_number = db.Column(db.String(50), nullable=False)
    representative_name = db.Column(db.String(255), nullable=False)
    representative_tc = db.Column(db.String(11), nullable=False)
    representative_title = db.Column(db.String(255), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
