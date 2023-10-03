from django.shortcuts import render
from django.http import JsonResponse

def main_url(request):
    return JsonResponse(data=f"Thanks for visting django using {request.get_host()}",safe=False)