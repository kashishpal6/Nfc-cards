from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import refer
from .serializers import ReferSubscriptionSerializer
from rest_framework.permissions import IsAuthenticated

class ReferSubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = refer.objects.all()
    serializer_class = ReferSubscriptionSerializer
    permission_classes =[IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   

