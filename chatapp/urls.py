from django.urls import path
from . import views

app_name = 'chatapp'


urlpatterns = [
    path('room', views.room), # ここにGETでroom一覧、POSTでroom作成
    path('message', views.message), # ここにGETでmessage一覧、POSTでmessage作成
    path('user', views.user), # ここにGETでuser一覧、POSTでuser作成
    path('message/<int:message_id>', views.message_detail), # GETでmessage1つ取得、PUTでmessage更新、DELETEでmessage削除
    path('get_user/<int:user_id>', views.get_user),
    path('get_messages_of_user/<int:user_id>', views.get_messages_of_user),
]
