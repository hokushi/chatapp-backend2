from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse, HttpResponse
from django.http.response import HttpResponse
from django.conf.urls.static import static
from django.conf import settings

def top_page_func(request):
    print('Hello World!!!')
    return HttpResponse('Hello World!!!')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello', top_page_func),
    path('chatapp/' , include('chatapp.urls'))
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
)