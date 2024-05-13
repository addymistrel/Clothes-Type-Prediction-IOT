from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import adafruit
import json

# Create your views here.
@api_view(['GET'])
def getData(request):
    return Response("my name is Aditya")

@api_view(['POST'])
def newData(request):
    # gotDataDic = json.loads(request.body.decode("utf-8"))
    # print(gotDataDic,type(gotDataDic))
    # newTrain = costGenerator.CostGenrator(int(gotDataDic["wagcap"]),int(gotDataDic["wagno"]),0,gotDataDic["graphPlot"])
    # result = newTrain.generateCost()
    # # print(result)
    # returnData = {"routePoints":result[0],"totalCost":result[1],"weightFull":result[2],"weightsEach":result[3],"stockFactor":result[4]}
    # print(returnData)
    print("Django Server Connection is OK")
    return Response("Django Server Connection is OK")

@api_view(['POST'])
def getTemperature(request):
    gotDataDic = json.loads(request.body.decode("utf-8"))
    print(gotDataDic,type(gotDataDic))
    result = int(adafruit.get_details(gotDataDic['key'])['last_value'][:-3])
    print(result)
    print("Django Server Connection is OK")
    return Response(result)

@api_view(['POST'])
def getHumidity(request):
    gotDataDic = json.loads(request.body.decode("utf-8"))
    print(gotDataDic,type(gotDataDic))
    result = int(adafruit.get_details(gotDataDic['key'])['last_value'][:-3])
    print(result)
    # print("Django Server Connection is OK")
    return Response(result)