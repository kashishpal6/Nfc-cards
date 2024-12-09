# from rest_framework import serializers, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from django.contrib.auth.models import User
# from .models import refer_subscription

# class ReferralSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = refer_subscription
#         fields = ['referrer', 'referred', 'created_at']

# class ReferralAPIView(APIView):
#     def post(self, request, *args, **kwargs):
#         referred_by = request.data.get("referred_by")
#         referred_to = request.data.get("referred_to")

        
#         if referre_id == referred_id:
#             return Response({"detail": "You cannot refer yourself."}, status=status.HTTP_400_BAD_REQUEST)

#         try:
#             referrer = User.objects.get(id=referrer_id)
#             referred = User.objects.get(id=referred_id)
#         except User.DoesNotExist:
#             return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

#         # Check if the referral already exists
#         if refer_subscription.objects.filter(referrer=referrer, referred=referred).exists():
#             return Response({"detail": "Referral already exists."}, status=status.HTTP_400_BAD_REQUEST)

#         # Create the referral
#         referral = refer_subscription.objects.create(referrer=referrer, referred=referred)
#         return Response(ReferralSerializer(referral).data, status=status.HTTP_201_CREATED)

from rest_framework import serializers
from .models import refer
from auth_app.models import CustomUser

class ReferSubscriptionSerializer(serializers.ModelSerializer):
    referred_by = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())
    referred_to = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = refer
        fields = ['referred_by', 'referred_to', 'start_date', 'end_date']

    def validate(self, attrs):
        referred_by = attrs.get('referred_by')
        referred_to = attrs.get('referred_to')


        if referred_by == referred_to:
            raise serializers.ValidationError("referred_by and referred_to cannot be the same user.")

        
        if refer.objects.filter(referred_to=referred_to).exists():
            raise serializers.ValidationError("This user has already been referred.")

        
        if CustomUser.objects.filter(id=referred_to.id).exists():
            raise serializers.ValidationError("Referred user already exists. Referral only works for new users.")

        return attrs



