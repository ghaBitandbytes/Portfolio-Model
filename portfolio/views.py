from rest_framework import generics
#generic from DRF ... 
# have pre-built classes that automatically handles CRUD logic..
#ListCreateAPIView : list and create (GET+POST)
#RetrieveUpdateDestroyAPIView : GET, PUT , PATCH DELETE
from .models import Portfolio
from .serializers import PortfolioSerializer
from django.shortcuts import render
from django.http import HttpResponse #importing http class 


def portfolio_home(request):
    return render(request, "index.html")

# Create your views here.
class PortfolioListCreateView(generics.ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class PortfolioDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer