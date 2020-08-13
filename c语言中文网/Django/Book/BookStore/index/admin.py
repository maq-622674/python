from django.contrib import admin
from index.models import Book, Author,UserInfo
#这个需要我们自己导入相应的模型类（数据表）
# Register your models here.


admin.site.register([Book,Author,UserInfo])
#admin.site.register(Book)