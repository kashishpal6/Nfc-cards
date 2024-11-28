from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import referSubscription
from .serializers import ReferSubscriptionSerializer

class ReferSubscriptionCreateAPIView(generics.CreateAPIView):
    queryset = referSubscription.objects.all()
    serializer_class = ReferSubscriptionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)