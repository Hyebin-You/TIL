from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomUserdetailSerializer
from .models import Usercard, Attacklist, Defenselist

# Create your views here.
@api_view(['GET'])
def user_detail(request):
    serializer = CustomUserdetailSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
def make_attacklist(request):
    ## form 데이터에 담긴 값들은 request.data['키값'] 으로 접근
    print(request.data['card1'])
    print(request.data['card2'])
    print(request.data['card3'])
    # card1 = get_object_or_404(Usercard, pk=request.data['card1'])
    # card2 = get_object_or_404(Usercard, pk=request.data['card2'])
    # card3 = get_object_or_404(Usercard, pk=request.data['card3'])

    # request.data['card1'] 값은 user.attacklist_set.card1 으로 호출 가능?