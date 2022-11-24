from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserdetailSerializer, UsercardSerializer
from .models import Usercard, Attacklist, Defenselist
from worlds.models import Card, Profile_icon
from worlds.serializers import ProfiliconSerializer
from movies.models import Genre

User = get_user_model()

# Create your views here.
@api_view(['GET'])
def user_detail(request):
    serializer = CustomUserdetailSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
def make_usercards(request):
    user = request.user
    card = Card.objects.get(pk=request.data['card_pk'])
    usercard = Usercard()
    usercard.cardname = card.cardname
    usercard.isnormal = card.isnormal
    usercard.attack = card.attack
    usercard.defense = card.defense
    usercard.life = card.life
    usercard.img_url = card.img_url
    usercard.ability1 = request.data['ability1']
    usercard.ability2 = request.data['ability2']
    usercard.ability3 = request.data['ability3']
    usercard.ability_grade = '에픽'
    usercard.user = user
    usercard.save()
    user.point -= 400
    user.save()
    serializer = UsercardSerializer(usercard)
    return Response(serializer.data)


@api_view(['POST'])
def make_attacklist(request):       # 공격덱 구성
    ## form 데이터에 담긴 값들은 request.data['키값'] 으로 접근
    card1 = get_object_or_404(Usercard, pk=request.data['card1'])
    card2 = get_object_or_404(Usercard, pk=request.data['card2'])
    card3 = get_object_or_404(Usercard, pk=request.data['card3'])

    al = request.user.attacklist_set.all()[0]
    al.card1 = card1
    al.card2 = card2
    al.card3 = card3
    al.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def make_defenselist(request):      # 방어 덱 구성
    card1 = get_object_or_404(Usercard, pk=request.data['card1'])
    card2 = get_object_or_404(Usercard, pk=request.data['card2'])
    card3 = get_object_or_404(Usercard, pk=request.data['card3'])

    dl = request.user.defenselist_set.all()[0]
    dl.card1 = card1
    dl.card2 = card2
    dl.card3 = card3
    dl.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST', 'PUT'])
def set_nickname(request):       # 회원가입 후 닉네임 집어넣기, 닉네임 수정
    users = User.objects.filter(nickname=request.data['nickname'])
    if len(users):
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        user = request.user
        user.nickname = request.data['nickname']
        user.save()
        if request.method == 'POST':
            al = Attacklist()
            al.user = user
            al.save()
            dl = Defenselist()
            dl.user = user
            dl.save()
        return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def set_like_genres(request, genre_name):
    genre = Genre.objects.get(name=genre_name)
    if not genre.like_users.filter(pk=request.user.pk).exists():
        genre.like_users.add(request.user)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def modify_card(request):
    card = Usercard.objects.get(pk=request.data['card_pk'])
    card.ability_grade = request.data['ability_grade']
    card.ability1 = request.data['ability1']
    card.ability2 = request.data['ability2']
    card.ability3 = request.data['ability3']
    card.save()
    serializer = UsercardSerializer(card)
    return Response(serializer.data)


@api_view(['POST'])
def use_cube(request):
    user = request.user
    if request.data['cubename'] == 'black':
        user.blackcube -= 1
    else:
        user.redcube -= 1
    
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def buy_icon(request):
    user = request.user
    price = request.data['price']
    icon = Profile_icon.objects.get(pk=request.data['icon_id'])
    if not icon.users.filter(pk=request.user.pk).exists():
        icon.users.add(user)
        user.point -= int(price)
        user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['PUT'])
def change_usericon(request):
    user = request.user
    icon_url = request.data['img_url']
    user.user_icon = icon_url
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def change_point(request):
    user = request.user
    point = request.data['point']
    if request.data['status'] == 'add':
        user.point += int(point)
    else:
        user.point -= int(point)
    user.save()
    return Response(status=status.HTTP_200_OK)