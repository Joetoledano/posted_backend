from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from util.db_util import get_deals, get_category_deals


@api_view(["GET"])
@authentication_classes([])
def deals(request):
    deals = get_deals()
    return Response(deals)

@api_view(["GET"])
@authentication_classes([])
def categories(request):
    primary = request.GET.get('primary')
    if not primary:
        return Response({'msg':'no primary'})
    secondary = request.GET.get('secondary')
    deals = get_category_deals(primary, secondary)
    return Response(deals)

@api_view(["GET"])
@authentication_classes([])
def check(request):
    return Response({"success": True})
