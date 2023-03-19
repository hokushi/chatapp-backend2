import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .models import Room
from .models import Message
from .models import UserProfile
from django.utils import timezone

@csrf_exempt
def room(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        data = []
        for room in rooms:
            data.append({
                'name': room.name,
                'id': room.id,
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        datas = json.loads(request.body)
        name = datas['name']
        Room.objects.create(name=name)
        return HttpResponse('room登録完了！')

@csrf_exempt
def message(request):
    if request.method == 'GET':
        # SQLを飛ばしている
        # select * from ChatappMessage
        messages = Message.objects.all() # list[ChatappMessage]
        data = []
        for message in messages:
            # message: ChatappMessage
            data.append({
                'message': { "text": message.content, "id": message.id },
                'sendername': message.user.username,
                'room': message.room.name,
                'created_at': [timezone.localtime(message.timestamp).month,
                               timezone.localtime(message.timestamp).day,
                               timezone.localtime(message.timestamp).hour,
                               timezone.localtime(message.timestamp).minute,
                               ]
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        datas = json.loads(request.body)
        chatappUser_id = datas['chatappUser_id']
        message = datas['message']
        # SQLを飛ばしている
        # insert into ChatappMessage (sendername_id, message) values (chatappUser_id, message)
        Message.objects.create(
            sendername=UserProfile.objects.get(id=chatappUser_id), message=message)
        return HttpResponse('message登録完了！')

@csrf_exempt
def message_detail(request, message_id):
    if request.method == 'GET':
        message = Message.objects.get(id=message_id)
        data = {
            'message': message.content,
            'sendername': message.user,
            'room': message.room,
            'created_at': [timezone.localtime(message.timestamp).month,
                           timezone.localtime(message.timestamp).day,
                           timezone.localtime(message.timestamp).hour,
                           timezone.localtime(message.timestamp).minute,]
        }
        return JsonResponse(data)

    if request.method == 'PUT':
        datas = json.loads(request.body)
        chatappUser_id = datas['chatappUser_id']
        message = datas['message']
        chat_app_message = Message.objects.get(id=message_id)
        chat_app_message.sendername = UserProfile.objects.get(id=chatappUser_id)
        chat_app_message.message = message
        chat_app_message.save()
        return HttpResponse("更新に成功しました")

    if request.method == 'DELETE':
        chat_app_message = Message.objects.get(id=message_id)
        chat_app_message.delete()
        return HttpResponse("削除に成功しました")



    

def get_user(request, user_id):
    user = UserProfile.objects.get(id=user_id)
    data = {
        'name': user.name,
        'id': user_id,
    }
    return JsonResponse(data)


@csrf_exempt
def user(request):
    if request.method == 'GET':
        users = UserProfile.objects.all()
        data = []
        for user in users:
            data.append({
                'name': user.name,
                'id': user.id,
            })
        return JsonResponse(data, safe=False)

    if request.method == 'POST':
        datas = json.loads(request.body)
        name = datas['name']
        UserProfile.objects.create(name=name)
        return HttpResponse('user登録完了！')




def get_messages_of_user(request, user_id):
    messages_list = UserProfile.objects.get(id=user_id).ChatappMessages.all()
    data = []
    for message in messages_list:
        data.append({
            'message': message.message,
            'sendername': message.sendername.name,
        })
    return JsonResponse(data, safe=False)
