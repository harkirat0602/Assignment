from django.shortcuts import render
import json
from django.http import JsonResponse

# Create your views here.


def API(request):
    # body_unicode = request.body.decode('utf-8')
    # body = json.loads(body_unicode)

    body = json.loads(request.body)

    zone = body["zone"]
    organization_id = body["organization_id"]
    total_distance = body["total_distance"]
    item_type = body["item_type"]

    if item_type=="perishable":
        after_price=1.5
    else:
        after_price=1

    total_price=10
    total_distance-=5
    if total_distance>0:
        total_price+= total_distance * after_price


    return JsonResponse({"total_price": total_price}, status=200)