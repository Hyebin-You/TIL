from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import RankSerializer, RankcommentSerializer, ProfiliconSerializer
from .models import Battlelog, Rankcomment, Profile_icon
from accounts.models import Defenselist, Attacklist
from accounts.serializers import DefenselistSerializer
import random


User = get_user_model()

# Create your views here.
@api_view(['GET'])
def ranklist(request):
    users = User.objects.all()
    userlist = []
    for user in users:
        if user.attacklist_set.all()[0].card1 != None:
            userlist.append(user)
    users = sorted(userlist, key=lambda x: (-x.win_point, len(x.battlelog_set.all())))
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
    
    enermy = User.objects.get(pk=request.data['enermy_id'])
    log.user = user
    log.my_card1_img = request.data['my1img']
    log.my_card2_img = request.data['my2img']
    log.my_card3_img = request.data['my3img']
    log.enermy_nickname = enermy.nickname
    log.enermy_card1_img = request.data['e1img']
    log.enermy_card2_img = request.data['e2img']
    log.enermy_card3_img = request.data['e3img']
    log.save()
    context = {
        'user_winpoint': user.win_point,
    }
    return JsonResponse(context)


@api_view(['GET'])
def rankcomment_list(request):
    rcomment_list = Rankcomment.objects.all().order_by('-pk')
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
        if user.point >= 100 * int(request.data['num']):
            user.blackcube += int(request.data['num'])
            user.point -= 100 * int(request.data['num'])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        if user.point >= 50 * int(request.data['num']):
            user.redcube += int(request.data['num'])
            user.point -= 50 * int(request.data['num'])
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)    
    user.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
def change_tier(request):       # 티어 변경 함수
    user = request.user
    user.tier = request.data['after']
    user.save()
    return Response(status=status.HTTP_200_OK)


def calculate_card(card):
    final_attack = card.attack
    final_defense = card.defense
    final_life = card.life
    a_a = 0
    a_l = 0
    a_list = [card.ability1, card.ability2, card.ability3]
    for a in a_list:
        if a[:2] == '공격':
            a_a += int(a[4:6])
        elif a[:2] == '방어':
            final_defense += int(a[4:6])
        else:
            a_l += int(a[3:5])

    final_attack += round(final_attack * a_a / 100)
    final_life += round(final_life * a_l / 100)
    card_info = {
        'isnormal': card.isnormal,
        'final_attack': final_attack,
        'final_defense': final_defense,
        'final_life' : final_life,
        'img_url': card.img_url
    }
    return card_info


@api_view(['GET'])
def get_enermy_status(request):
    defenselists = Defenselist.objects.exclude(user_id=request.user.pk)
    defenselists = defenselists.exclude(card1_id=None)
    defenselist = random.sample(list(defenselists), 1)
    enermy_nickname = defenselist[0].user.nickname
    c1_info = calculate_card(defenselist[0].card1)
    c2_info = calculate_card(defenselist[0].card2)
    c3_info = calculate_card(defenselist[0].card3)
    enermy_status = {
        'enermy_id': defenselist[0].user.id,
        'enermy_nickname': enermy_nickname,
        'card1': c1_info,
        'card2': c2_info,
        'card3': c3_info
    }
    return JsonResponse(enermy_status)


@api_view(['GET'])
def get_my_status(request):
    if request.user.attacklist_set.all()[0].card1 == None:
        my_status = {
            'my_nickname': request.user.nickname,
            'card1': None,
            'card2': None,
            'card3': None
        }
        return JsonResponse(my_status)

    attacklist = Attacklist.objects.get(user_id=request.user.pk)
    c1_info = calculate_card(attacklist.card1)
    c2_info = calculate_card(attacklist.card2)
    c3_info = calculate_card(attacklist.card3)
    my_status = {
        'my_nickname': request.user.nickname,
        'card1': c1_info,
        'card2': c2_info,
        'card3': c3_info
    }
    return JsonResponse(my_status)


@api_view(['GET'])
def iconlists(request):
    icons = Profile_icon.objects.all().order_by('price')
    serializer = ProfiliconSerializer(icons, many=True)
    return Response(serializer.data)