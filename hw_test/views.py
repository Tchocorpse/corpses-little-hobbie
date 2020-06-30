from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import HelloTestMessage
from .forms import TestMessageRecieve
from django.utils import timezone
from django.views import View


class ReceiveTestMessage(View):
    def post(self, request):

        return HttpResponseRedirect("/hw_test/Test_separate_input")

    def get(self, request):
        message_head = HelloTestMessage.objects.all()

        return render(
            request, "hw_test/index.html", context={"messages_list": message_head,},
        )


class ReceiveDeleteMessage(View):
    def post(self, request, delete_id):

        delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
        delete_hello.delete()

        return HttpResponseRedirect("/hw_test/")

    def get(self):
        return HttpResponseRedirect("/hw_test/")


class SeparateDetailed(View):
    def get(self, request, detail_id):
        detail_hello = get_object_or_404(HelloTestMessage, pk=detail_id)

        return render(
            request,
            "hw_test/Test_detail.html",
            context={"hello_message": detail_hello,},
        )

    # else:
    # return HttpResponseRedirect("/hw_test/")


class SeparateInput(View):
    received_message = HelloTestMessage()
    test_form_class = TestMessageRecieve

    def post(self, request):
        test_form = self.test_form_class(request.POST)

        if test_form.is_valid():

            self.received_message.hello_title = test_form.cleaned_data["hello_title"]
            self.received_message.hello_body = test_form.cleaned_data["hello_body"]
            self.received_message.publishing_date = timezone.now()

            self.received_message.save()

            return HttpResponseRedirect("/hw_test/")
            # return render(
            #    request, "hw_test/index.html", context={"form": test_form, "messages_list": message_head, }
            # )
        else:

            return HttpResponseRedirect("/hw_test/")

    def get(self, request):
        test_form = self.test_form_class()
        message_head = HelloTestMessage.objects.all()

        # return HttpResponseRedirect("/hw_test/")
        return render(
            request,
            "hw_test/Test_separate_input.html",
            context={"form": test_form, "messages_list": message_head,},
        )
