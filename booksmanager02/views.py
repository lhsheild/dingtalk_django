from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
class Main(View):
    def get(self, request):
        data = {'test': 'include url'}
        return JsonResponse(data=data)