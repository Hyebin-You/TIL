from django.shortcuts import render
# from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RankSerializer, RankcommentSerializer
from .models import Battlelog, Rankcomment


User = get_user_model()

# Create your views here.
@api_view(['GET'])
def ranklist(request):
    users = User.objects.all()
    print(users[0].battlelog_set.all())
    users = sorted(users, key=lambda x: (-x.win_point, len(x.battlelog_set.all())))
    serializer = RankSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def make_battlelog(request):
    user = request.user
    
    if request.data['log'] == '승':
        user.win_point += 100
        user.save()
        log = Battlelog()
        log.log = '승리'
    else:
        if user.win_point >= 50:
            user.win_point -= 50
        user.save()
        log = Battlelog()
        log.log = '패배'
    
    log.enermy_id = request.data['enermy_id']
    log.user = user
    log.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def rankcomment_list(request):
    rcomment_list = Rankcomment.objects.all()
    serializer = RankcommentSerializer(rcomment_list, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_rankcomment(request):
    rcomment = Rankcomment()
    rcomment.content = request.data['content']
    rcomment.save()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['POST'])
def buy_cube(request):
    user = request.user

    if request.data['cubename'] == 'black':
        user.blackcube += 1
        user.point -= 100
    else:
        user.redcube += 1
        user.point -= 50
    
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def change_tier(request):       # 티어 변경 함수
    user = request.user
    user.tier = request.data['after']
    user.save()
    return Response(status=status.HTTP_200_OK)