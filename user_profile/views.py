from django.shortcuts import render
from rest_framework.response import Response
from user_profile.models import UserProfile
from user_profile.serializers import UserProfileSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def user_profile_collection(request):
    if request.method == 'GET':
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profiles, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def user_profile_element(request, pk):
    try:
        user_profile = UserProfile.objects.get(pk=pk)
    except UserProfile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserProfileSerializer(user_profile)
        return Response(serializer.data)


class HelloView(APIView):
    serializer_class = UserProfileSerializer
    def get(self, request, format=None):
        """Retruns a list of APIViews features."""

        an_apiview = [
            'Uses HTTP methods as fucntion (get, post, patch, put, delete)',
            'It is similar to a traditional Django view',
            'Gives you the most of the control over your logic',
            'Is mapped manually to URLs'
        ]
        user_profiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(user_profiles, many=True)
        #The response must be as dictionary which will be shown in json as response
        return Response({'message': 'Hello!', 'an_apiview': an_apiview, 'data':serializer.data})



    def post(self,request):
        serializer = UserProfileSerializer(data=request.data)
        if serializer.is_valid():
                message = 'data saved'
                serializer.save()
                return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)