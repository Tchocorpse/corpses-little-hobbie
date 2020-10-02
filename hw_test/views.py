from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.views import APIView

import logging

from .forms import TestMessageRecieve
from .models import HelloTestMessage
from .serializers import TestMessageSerializer


class ReceiveTestMessage(APIView):
    def get(self, request, *args, **kwargs):
        message_head = HelloTestMessage.objects.all()
        if request.GET.get("front"):

            message_head_serialized = TestMessageSerializer(message_head, many=True)
            return JsonResponse({"MesHe": message_head_serialized.data}, status=200)

        else:
            return render(
                request, "hw_test/index.html", context={"messages_list": message_head,},
            )


class ReceiveDeleteMessage(APIView):
    def get(self, request, delete_id):

        if request.GET.get("front"):
            #logging.warning(request.GET)
            delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
            delete_hello.delete()
            return HttpResponse(status=200)
        else:
            # Strange legacy
            # delete_flag = request.GET.get('delete_flag', 0)
            delete_flag = True
            if delete_flag:

                delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
                delete_hello.delete()

            return HttpResponseRedirect("/hw_test/")


class SeparateDetailed(APIView):
    def get(self, request, detail_id):
        detail_hello = get_object_or_404(HelloTestMessage, pk=detail_id)

        return render(
            request,
            "hw_test/Test_detail.html",
            context={"hello_message": detail_hello,},
        )


class SeparateInput(APIView):
    test_form_class = TestMessageRecieve

    def post(self, request):

        if request.GET.get("front"):

            received_serialized_message = TestMessageSerializer(data=request.data)
            if received_serialized_message.is_valid():
                received_serialized_message.save()
                return HttpResponse(status=201)

            else:
                return HttpResponse(status=400)
        else:
            test_form = self.test_form_class(request.POST)
            if test_form.is_valid():
                received_message = HelloTestMessage.objects.create(
                    **test_form.cleaned_data
                )
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


class SeparateRecent(APIView):

    def get(self, request):
        recent_hello = HelloTestMessage.objects.order_by("-publishing_dt").first()

        return render(
            request,
            "hw_test/Test_recent.html",
            context={"hello_message": recent_hello,},
        )


class SeparateImageInput(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):

        if request.GET.get("front"):
            uploaded_image = request.data
            logging.warning(uploaded_image)
            return HttpResponse(status=201)
        else:
            return HttpResponse(status=400)
