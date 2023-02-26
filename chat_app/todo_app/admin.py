from django.contrib import admin
from .models import Todo  # Todoクラスのインポート

# Register your models here.
admin.site.register(Todo)  # Todoモデルの追加
