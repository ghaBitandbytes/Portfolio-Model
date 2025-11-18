#serializers needed because RESTAPi works in JSON but model is python object so serializer convert the python object in json to made it suitable for restapi
from rest_framework import serializers
from .models import Portfolio

class PortfolioSerializer(serializers.ModelSerializer):#modelserializer automatically cretae fields based on oyur model do not need to create manually 
    class Meta:
        model = Portfolio
        fields = '__all__' #tells to include all fields in th portfolio model in the API