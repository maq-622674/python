'''
该应用后台管理系统配置
'''
from django.contrib import admin
from .models import Post, Category

admin.site.register(Post)
admin.site.register(Category)
