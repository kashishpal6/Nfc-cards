from .models import ReturnPage
from .serializers import ReturnPageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class createReturnPage(generics.CreateAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAuthenticated]
    
class listReturnPage(generics.ListAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAdminUser]

class retrieveReturnPage(generics.RetrieveAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAuthenticated]
    
class updateReturnPage(generics.UpdateAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAdminUser]


