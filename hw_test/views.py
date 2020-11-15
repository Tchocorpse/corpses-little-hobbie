from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FileUploadParser, MultiPartParser
from rest_framework.views import APIView

import logging

from .forms import TestMessageRecieve
from .models import HelloTestMessage, ImageFileModel, MessageImageMap
from .serializers import (
    TestMessageSerializer,
    MessageImageMapSerializer,
    ImageFileSerializer,
)


class ReceiveMessage(APIView):
    def get(self, request, *args, **kwargs):
        messages_list = HelloTestMessage.objects.all()

        message_list_serialized = TestMessageSerializer(messages_list, many=True)
        return JsonResponse({"MesHe": message_list_serialized.data}, status=200,)


class ReceiveDeleteMessage(APIView):
    def get(self, request, delete_id):

        delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
        delete_hello.delete()

        image_map = get_object_or_404(MessageImageMap, message_id=delete_id)
        image_map_serialized = MessageImageMapSerializer(image_map)
        image_map.delete()

        image_to_delete_id = image_map_serialized.data["image_id"]
        if image_to_delete_id != -1:
            image_to_delete = ImageFileModel.objects.get(pk=image_to_delete_id)
            image_to_delete.delete()

        return HttpResponse(status=200)


class SeparateInput(APIView):
    # serializer_class = TestMessageSerializer
    message_id = -1
    image_id = -1

    def post(self, request):

        message_data = {
            "hello_title": request.data["hello_title"],
            "hello_body": request.data["hello_body"],
        }
        image_data = {"image_file": request.data["file"]}
        logging.warning(message_data)
        received_serialized_message = TestMessageSerializer(data=message_data)
        received_serialized_image = ImageFileSerializer(data=image_data)

        if (
            received_serialized_message.is_valid()
            and received_serialized_image.is_valid()
        ):
            received_serialized_message.save()
            received_serialized_image.save()

            message_id = received_serialized_message.data["id"]
            image_id = received_serialized_image.data["id"]

            self.message_id = message_id
            self.image_id = image_id
            self.save_mi_map()

            return HttpResponse(status=201)

        elif received_serialized_message.is_valid():
            received_serialized_message.save()
            message_id = received_serialized_message.data["id"]
            self.message_id = message_id
            self.save_mi_map()
            return HttpResponse(status=201)

        else:
            return HttpResponse(status=400)

    def save_mi_map(self):
        mi_map = {"message_id": self.message_id, "image_id": self.image_id}
        mi_map_serializer = MessageImageMapSerializer(data=mi_map)
        if mi_map_serializer.is_valid():
            mi_map_serializer.save()


class SeparateImageOutput(APIView):
    def get(self, request, message_id):
        image_map = get_object_or_404(MessageImageMap, message_id=message_id)
        image_map_serialized = MessageImageMapSerializer(image_map)
        image_to_send_id = image_map_serialized.data["image_id"]
        if image_to_send_id != -1:
            image_to_send = ImageFileModel.objects.get(pk=image_to_send_id)
            image_to_send_serialized = ImageFileSerializer(image_to_send)
            return HttpResponse(
                image_to_send_serialized.data["image_file"], content_type="image/jpg"
            )
        else:
            return HttpResponse(status=400)


# ###################################################### Legacy part #############################################


class SeparateRecent(APIView):
    def get(self, request):
        recent_hello = HelloTestMessage.objects.order_by("-publishing_dt").first()

        return render(
            request,
            "hw_test/Test_recent.html",
            context={"hello_message": recent_hello,},
        )


class LegacyInput(APIView):
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

        return render(
            request,
            "hw_test/Test_separate_input.html",
            context={"form": test_form, "messages_list": message_head,},
        )


class SeparateDetailed(APIView):
    def get(self, request, detail_id):
        detail_hello = get_object_or_404(HelloTestMessage, pk=detail_id)

        return render(
            request,
            "hw_test/Test_detail.html",
            context={"hello_message": detail_hello,},
        )


class LegacyDeleteMessage(APIView):
    def get(self, request, delete_id):
        # Strange legacy
        # delete_flag = request.GET.get('delete_flag', 0)
        delete_flag = True
        if delete_flag:
            delete_hello = get_object_or_404(HelloTestMessage, pk=delete_id)
            delete_hello.delete()

        return HttpResponseRedirect("/hw_test/")


class LegacyReceiveMessage(APIView):
    def get(self, request, *args, **kwargs):
        messages_list = HelloTestMessage.objects.all()
        return render(
            request, "hw_test/index.html", context={"messages_list": messages_list,},
        )
