from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import HelloTestMessage
from .forms import TestMessageRecieve
from django.utils import timezone


#def index(request):

    #message_head = HelloTestMessage.objects.all()

   # return render(
   #     request, "hw_test/index.html", context={"messages_list": message_head,}
   # )
    # return HttpResponse("Hello, world and you Цыма. I am test app. Give me your response.")

class TestMessageTemplate():
    def __init__(self, hello_title, hello_body, publishing_date = 0):
        self.hello_title = hello_title
        self.hello_body = hello_body
        self.publishing_date = publishing_date



def receive_test_message(request):
    if request.method == "POST":
        test_form = TestMessageRecieve(request.POST)

        if test_form.is_valid():

            received_message = HelloTestMessage()
            received_title = "debug title"
            received_body = "debug body"
            #received_message = TestMessageTemplate(received_title, received_body)
            received_message.hello_title = test_form.cleaned_data['hello_title']
            received_message.hello_body = test_form.cleaned_data['hello_body']
            received_message.publishing_date = timezone.now()
            #received_list = [received_message]
            received_message.save()



            return HttpResponseRedirect("/hw_test/")
            #return render(
            #    request, "hw_test/index.html", context={"form": test_form, "messages_list": message_head, }
            #)

    else:
        test_form = TestMessageRecieve()
    message_head = HelloTestMessage.objects.all()


    #return HttpResponseRedirect("/hw_test/")
    return render(
        request, "hw_test/index.html", context={"form": test_form, "messages_list": message_head, }
    )