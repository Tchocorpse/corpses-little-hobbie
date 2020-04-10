from django.http import HttpResponse
from django.shortcuts import render
from .models import HelloTestMessage


def index(request):

    messages_list = HelloTestMessage.objects.all()
    return render(
        request, "hw_test/index.html", context={"messages_list": messages_list,}
    )
    # return HttpResponse("Hello, world and you Цыма. I am test app. Give me your response.")
