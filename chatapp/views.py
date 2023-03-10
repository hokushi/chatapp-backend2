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
        'id': user_id,
    }
    return JsonResponse(data)


@csrf_exempt
def message(request):
    if request.method == 'GET':
        # SQLを飛ばしている
        # select * from ChatappMessage
        messages = ChatappMessage.objects.all() # list[ChatappMessage]
        data = []
        for message in messages:
            # message: ChatappMessage
            data.append({
                'message': { "text": message.message, "id": message.id },
                'sendername': message.sendername.name,
                'sendername_id': message.sendername.id,
                'created_at': [timezone.localtime(message.created_at).month,
                               timezone.localtime(message.created_at).day,
                               timezone.localtime(message.created_at).hour,
                               timezone.localtime(message.created_at).minute,
                               ]
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        datas = json.loads(request.body)
        chatappUser_id = datas['chatappUser_id']
        message = datas['message']
        # SQLを飛ばしている
        # insert into ChatappMessage (sendername_id, message) values (chatappUser_id, message)
        ChatappMessage.objects.create(
            sendername=ChatappUser.objects.get(id=chatappUser_id), message=message)
        return HttpResponse('message登録完了！')


@csrf_exempt
def message_detail(request, message_id):
    if request.method == 'GET':
        message = ChatappMessage.objects.get(id=message_id)
        data = {
            'message': message.message,
            'sendername': message.sendername.name,
            'sendername_id': message.sendername.id,
            'created_at': [timezone.localtime(message.created_at).month,
                           timezone.localtime(message.created_at).day,
                           timezone.localtime(message.created_at).hour,
                           timezone.localtime(message.created_at).minute,]
        }
        return JsonResponse(data)

    if request.method == 'PUT':
        datas = json.loads(request.body)
        chatappUser_id = datas['chatappUser_id']
        message = datas['message']
        chat_app_message = ChatappMessage.objects.get(id=message_id)
        chat_app_message.sendername = ChatappUser.objects.get(id=chatappUser_id)
        chat_app_message.message = message
        chat_app_message.save()
        return HttpResponse("更新に成功しました")

    if request.method == 'DELETE':
        chat_app_message = ChatappMessage.objects.get(id=message_id)
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
