from django.db import models

# Create your models here.

BRAND_CHOICES = [
    ('Mikrotik', 'Mikrotik'),
    ('TPLink', 'TPLink'),
    ('HPE', 'HPE'),
    ('Unifi', 'Unifi'),
    ('Draytek','Draytek'),
    ('Camera', 'Camera'),
    ('Linksys','Linksys'),
    ('Other', 'Other'),
]
CLASSIFY_CHOICES = [
    ('Router', 'Router'),
    ('Wifi', 'Wifi'),
    ('Camera', 'Camera'),
    ('Switch/Hub', 'Switch/Hub'),
    ('Other', 'Other'),
]
STATTUS_CHOICES = [
    ('Còn hàng', 'Còn hàng'),
    ('Hết hàng', 'Hết hàng'),
    ('Othe', 'Other'),
]



class Product(models.Model):
    name = models.CharField(max_length=300)
    code_number = models.CharField(max_length=100, default='brand+năm+số TT 2 số (ex: mikrotik202101)')
    brand = models.CharField(max_length=100, choices=BRAND_CHOICES, default='Other')
    classify=models.CharField(max_length=200,choices=CLASSIFY_CHOICES,default='Other',null=True)
    status = models.CharField(max_length=100, choices=STATTUS_CHOICES, default='Còn hàng')
    price = models.CharField(max_length=50, default='Nhập giá VNĐ')
    summary=models.TextField(max_length=150,null=True)
    description = models.TextField()
    picture1 = models.ImageField( upload_to='static/images/pictue_up')  # chú ý ko thêm thuộc tính Heigh, width cho image khi save báo lỗi Name not string
    picture2 = models.ImageField(upload_to='static/images/pictue_up', null=True)
    data_sheet = models.FileField(upload_to='static/images/file_up', null=True)

    def __str__(self):
        return self.name
    def image_str(self):
        return (self.picture1)
