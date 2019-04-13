from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from posted.api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from util.db_util import get_deals



@api_view(["GET"])
@authentication_classes([])
def userview(request):
    queryset = User.objects.all().order_by('-date_joined')
    serialized = UserSerializer(queryset, many=True)
    return Response({'data':serialized.data})

@api_view(["GET"])
@authentication_classes([])
def deals(request):
    deals = get_deals()
    return Response(deals)

@api_view(["GET"])
@authentication_classes([])
def groupview(request):
    queryset = Group.objects.all()
    serialized =  GroupSerializer(queryset, many=True)
    return Response({'data':serialized.data})


@api_view(["GET"])
@authentication_classes([])
def check(request):
    return Response({"success": True})
