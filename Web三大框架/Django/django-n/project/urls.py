"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
##################################################################################################################################################
########################################URL配置文件 Django项目中所有地址中（页面）都需要我们自己去配置其URL#############################################
###################################################################################################################################################
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('nblog3.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
'''
urls.py路由配置(URLConf)

URL配置(URLconf)就像Django 所支撑网站的目录。它的本质是URL与要为该URL调用的视图函数之间的映射表。 
基本格式：
Django1.x版本：
from django.conf.urls import url
#循环urlpatterns，找到对应的函数执行,匹配上一个路径就找到对应的函数执行，就不再往下循环了，并给函数传一个参数request，和wsgiref的environ类似，就是请求信息的所有内容
urlpatterns = [
     url(正则表达式, views视图函数，参数),
]
 

Django2.x版本：
from django.urls import path 
urlpatterns = [
    path('articles/2003/', views.special_case_2003),
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
]  
参数说明

· 正则表达式：一个正则表达式字符串

· views视图函数：一个可调用对象，通常为一个视图函数或一个指定视图函数路径的字符串

·  参数：可选的要传递给视图函数的默认参数（字典形式）
'''