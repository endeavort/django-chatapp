from django.shortcuts import render, redirect  # レンダリング、リダイレクト機能のインポート
from django.views import View  # Viewクラスのインポート
from todo_app.models import Todo  # Todoクラスのインポート

# Create your views here.
# トップ画面
class IndexView(View):

    # Getリクエストの時の処理
    def get(self, request):
        # DBから更新日時降順でTODOを取得してテンプレートに返す
        todos = Todo.objects.all().order_by("-updated_at")
        # render(request, パス, 渡したいデータ（辞書形式))
        return render(request, "todo/index.html", {"todos": todos})

    # Postリクエストの時の処理
    def post(self, request):
        # フォームに記載された内容をデータベースに記録する
        memo = request.POST["memo"]
        todo = Todo(memo=memo)
        todo.save()
        # リダイレクト(別のページに転送する)
        return redirect("/")
