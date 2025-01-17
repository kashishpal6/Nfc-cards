from .models import ReturnPage
from .serializers import ReturnPageSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.exceptions import NotFound

class createReturnPage(generics.CreateAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user  
        serializer.save(user=user)
    
class listReturnPage(generics.ListAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAdminUser]

class retrieveReturnPage(generics.RetrieveAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        try:
            return ReturnPage.objects.get(user=self.request.user)
        except ReturnPage.DoesNotExist:
            raise NotFound(detail="Not any Purchase")
    
class updateReturnPage(generics.UpdateAPIView):
    queryset = ReturnPage.objects.all()
    serializer_class = ReturnPageSerializer
    permission_classes = [IsAdminUser]

    def get_object(self):
        try:
            return ReturnPage.objects.get(user=self.request.user)
        except ReturnPage.DoesNotExist:
            raise NotFound(detail="Profile not found")

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


