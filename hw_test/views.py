from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse

from .forms import TestMessageRecieve
from .models import HelloTestMessage


class ReceiveTestMessage(View):
    def get(self, request, *args, **kwargs):

        message_head = HelloTestMessage.objects.all()
        if kwargs.get('front') == 1:
            return JsonResponse({'MesHe': message_head}, status=200)
        else:
            return render(
                request, "hw_test/index.html", context={"messages_list": message_head,},
            )


class ReceiveDeleteMessage(View):
    # def post(self, request, delete_id):

    # return HttpResponseRedirect("/hw_test/")

    def get(self, request, delete_id):

        # delete_flag = request.GET.get('delete_flag', 0)
        delete_flag = True
        if delete_flag:

            delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
            delete_hello.delete()

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
    #received_message = HelloTestMessage()
    test_form_class = TestMessageRecieve

    def post(self, request):
        test_form = self.test_form_class(request.POST)

        if test_form.is_valid():


            received_message = HelloTestMessage.objects.create(**test_form.cleaned_data)


            received_message.save()

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


class SeparateRecent(View):
    def get(self, request):
        recent_hello = HelloTestMessage.objects.order_by("-publishing_dt").first()

        return render(
            request,
            "hw_test/Test_recent.html",
            context={"hello_message": recent_hello,},
        )
