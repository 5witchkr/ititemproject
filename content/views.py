from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed
from rest_framework.response import Response


# Create your views here.

class Main(APIView):
    def get(self, request):
        feedList = Feed.objects.all()

        return render(request, "newsitepin/main.html", context=dict(feedList=feedList))#파이썬dict형식은 json과 호환이됨

class CreateMain(APIView):
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')

        Feed.objects.create(content=content, title=title)

        return Response(status=200,data=dict(resultCode=0, resultMsg="success"))