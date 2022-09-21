from .serializers import *
from customers.models import *
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status


class CustomersViewSet(viewsets.ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()
    def get(self, format=None):

        Customers = Customers.objects.all()
        serializer = CustomersSerializer(Customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomersSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)