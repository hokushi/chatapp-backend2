import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import ChatappUser
from .models import ChatappMessage
from django.utils import timezone


def get_user(request, user_id):
    user = ChatappUser.objects.get(id=user_id)
    data = {
        'name': user.name,
        'id':user_id,
    }
    return JsonResponse(data)

@csrf_exempt
def message(request):
    if request.method == 'GET':
        messages = ChatappMessage.objects.all()
        data = []
        for message in messages:
            data.append({
                'message': message.message,
                'sendername': message.sendername.name,
                'sendername_id': message.sendername.id,
                'created_at': [timezone.localtime(message.created_at).hour,
                            timezone.localtime(message.created_at).minute,]
            })
        return JsonResponse(data, safe=False)
    
    if request.method == 'POST':
        datas = json.loads(request.body)
        chatappUser_id = datas['chatappUser_id']
        message = datas['message']
        ChatappMessage.objects.create(sendername=ChatappUser.objects.get(id=chatappUser_id), message=message)
        return HttpResponse('message登録完了！')

    if request.method == 'DELETE':
        chat_app_message = ChatappMessage.objects.get(id=user_id)
        chat_app_message.delete()
        return HttpResponse("削除に成功しました")

def get_messages_of_user(request, user_id):
    messages_list = ChatappUser.objects.get(id=user_id).ChatappMessages.all()
    data = []
    for message in messages_list:
        data.append({
            'message': message.message,
            'sendername': message.sendername.name,
        })
    return JsonResponse(data, safe=False)