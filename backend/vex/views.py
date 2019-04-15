from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from .utils import generateId
from .ml import predict
from PIL import Image
from io import BytesIO
import os
import base64

filepath = "static/images"

class VexView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(VexView, self).dispatch(request, *args, **kwargs)

    def post(self, request):

        image = request.body.decode("utf-8").lstrip("data:image/png;base64")
        sample = Image.open(BytesIO(base64.urlsafe_b64decode(image)))
        data = predict(sample)
        sample.close()

        return JsonResponse(data)

    def saveImage(self, request):

        image = request.body.decode("utf-8").lstrip("data:image/png;base64")
        id = generateId()

        with open(os.path.join(filepath, id + ".png"), "wb+") as file:
            file.write(base64.urlsafe_b64decode(image))

        with open(os.path.join("static", "test.csv"), "a+") as file:
            file.write(id + ",\n")

        response = HttpResponse()
        response.write("<p>Image Saved.</p>")

        return response