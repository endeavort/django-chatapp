from django.db import models

# Create your models here.
class Todo(models.Model):
    memo = models.TextField()  # todoの内容を保持するフィールド（テキスト）
    is_done = models.BooleanField(default=False)  # 処理済みかどうかを管理(True or False)
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日時を保持(日付型)
    updated_at = models.DateTimeField(auto_now=True)  # 更新日時を保持（日付型）
