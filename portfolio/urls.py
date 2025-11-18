from django.urls import path
from .views import PortfolioListCreateView, PortfolioDetailView, portfolio_home

urlpatterns = [
    path('', PortfolioListCreateView.as_view(), name='portfolio-list-create'),# List all portfolios + Create new portfolio, name thing is just an identifier for this path ... like a nickname 
    path('<int:pk>/', PortfolioDetailView.as_view(), name='portfolio-detail'),# Retrieve, Update, Delete a portfolio by ID
    path('home/', portfolio_home, name='portfolio-home')
]
