from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
# model = pickle.load(open('model.pkl','rb'))

# Create your views here.
@api_view(['GET'])
def getData(request):
    return Response("my name is Aditya")

@api_view(['POST'])
def newData(request):
    return Response("my name is Aditya")

@api_view(['POST'])
def mloutput(request):
    gotDataDic = json.loads(request.body.decode("utf-8"))
    print(gotDataDic,type(gotDataDic))
    return Response("my name is Aditya")