from django.shortcuts import render,get_object_or_404,HttpResponse
from .serializers import UserSerializer,UserProfileSerializer
from .models import Profile,User
from django.contrib.auth.models import User
from rest_framework import generics,mixins
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login as user_login
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from django.core import exceptions
from rest_framework.parsers import JSONParser

# ====================================================== Generic CreateAPIVie ==========================================
class UserCreateGenericAPI(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    """ user signing up here with defauld User fields and token also generating  """
    def post(self, request, *args, **kwargs):

        serailzie_data = UserSerializer(data=request.data)
        if serailzie_data.is_valid(raise_exception=True):
            user = serailzie_data.save()
            token,create = Token.objects.get_or_create(user=user)

            data = {
                'token : ':token.key,
            }
            return Response(data,status=200)


# ================================================== Generic UpdateAPIView and mixins ====================================
class UserUpdateGenericAPI(generics.UpdateAPIView,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin):

    queryset = Profile.objects.all()
    serializer_class = UserProfileSerializer
    lookup_field = "id"

    """ getting data from Profile database with of without login id"""
    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    """ updating profile data  """
    def put(self, request, id=None):
        return self.update(request, id)

    """ creating or inserting new user to profile database"""
    def post(self,request,id=None):
        return self.create(request)

    """ deleting user from profile database"""
    def delete(self,request,id=None):
        return self.destroy(request,id)



# ============================================== user authenticate loggin APIView ==================================
class LoginApiView(APIView):

    """"" this function authentcate user and genrating the user token """
    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        password = request.data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                user_login(request, user)
                token, create = Token.objects.get_or_create(user=user)

# =========================== below matchig the user form User and Profile models to get all info ======================
                profile_data = Profile.objects.get(user = token.user)
                user_data = User.objects.get(username = token.user)
# =====================================================================================================================

                context = {
                 # ============== below data from User object(user_data)=========
                    'username ': user_data.username,
                    'first_name ': user_data.first_name,
                    'second_name ': user_data.last_name,
                    'password ': user_data.password,

                # ============= below from Profile object(profile_data =============
                    'cnic ':profile_data.cnic,
                    'address ':profile_data.address,
                    'phone ':profile_data.phone,
                    'token ': token.key,

                }
                return Response(context, status=200)
            else:
                raise exceptions.ValidationError("Given credentials not correct")
        else:
            raise exceptions.ValidationError("username and password must be provided")

