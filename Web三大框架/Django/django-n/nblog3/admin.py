'''
该应用后台管理系统配置
admin.py：django自带的后台管理操作需要再此处实现
'''
from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
