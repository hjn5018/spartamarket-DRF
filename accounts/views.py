from accounts.models import User
from accounts.serializers import AccountSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['POST'])
def signup(request):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def profile(request, username):
    user = User.objects.get(username=username)
    if request.user == user:
        result = {
            'username':request.user.username,
            'date_joined':request.user.date_joined,
            'email':request.user.email,
            'name':request.user.name,
            'nickname':request.user.nickname,
            'birth_date':request.user.birth_date,
            'gender':request.user.gender,
            'introduce':request.user.introduce,
        }
        return Response(result)