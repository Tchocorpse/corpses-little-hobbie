from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import HelloTestMessage
from .forms import TestMessageRecieve
from django.utils import timezone
from django.urls import reverse


def receive_test_message(request):
    if request.method == "POST":
        test_form = TestMessageRecieve(request.POST)

        if test_form.is_valid():

            received_message = HelloTestMessage()

            received_message.hello_title = test_form.cleaned_data["hello_title"]
            received_message.hello_body = test_form.cleaned_data["hello_body"]
            received_message.publishing_date = timezone.now()

            received_message.save()

            return HttpResponseRedirect("/hw_test/")
            # return render(
            #    request, "hw_test/index.html", context={"form": test_form, "messages_list": message_head, }
            # )
        else:

            return HttpResponseRedirect("/hw_test/")
    else:
        test_form = TestMessageRecieve()
        message_head = HelloTestMessage.objects.all()

        # return HttpResponseRedirect("/hw_test/")
        return render(
            request,
            "hw_test/index.html",
            context={"form": test_form, "messages_list": message_head,},
        )


def receive_delete_message(request, delete_id):
    if request.method == "POST":
        delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)

        delete_hello.delete()
        return HttpResponseRedirect("/hw_test/")

    else:
        return HttpResponseRedirect("/hw_test/")
