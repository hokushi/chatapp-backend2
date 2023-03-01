from django.urls import path
from . import views

app_name = 'chatapp'


urlpatterns = [
    path('message', views.message),  # ここにGETでmessage一覧、POSTでmessage作成
    # GETでmessage1つ取得、PUTでmessage更新、DELETEでmessage削除
    path('message/<int:message_id>', views.message_detail),
    path('get_user/<int:user_id>', views.get_user),
    path('get_messages_of_user/<int:user_id>', views.get_messages_of_user),
    path('message_apiview', views.MessageView.as_view()),
    path('message_detail_apiview/<int:message_id>',
         views.MessageDetailView.as_view())
]
