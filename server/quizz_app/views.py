from django.shortcuts import render
from rest_framework.generics import RetrieveUpdateAPIView
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
import moncashify
import random
import string
from .serializers import *
from .models import *
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError, mail_admins
from time import gmtime, strftime
from django.db.models import F
from knox.models import AuthToken
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

def view_404(request, exception=None):
    # make a redirect to homepage
    # you can use the name of url or just the plain link
    return redirect('/') # or redirect('name-of-index-url')

def index(request):
    return HttpResponse("<h1>It 's private</h1>")

def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))


class WalletView(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except:
            return None

    def get(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = Wallet.objects.get(user=pk)
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            user = Wallet.objects.get(user=tokenview)
        if not user:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})

        # You have a serializer that you specified which fields should be available in fo
        serializer = WalletSerializer(user)
        # And here we send it those fields to our react component as json
        # Check this json data on React side, parse it, render it as form.
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = Profile.objects.get(user=pk)
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            user = User.objects.get(pk=tokenview)
        montant = request.data.get("montant", None)
        montant1 = request.data.get("montant1", None)
        getwallet = Wallet.objects.get(user=user)
        if montant:
            if int(getwallet.montant) >= int(montant):
                Wallet.objects.filter(user=user).update(montant=F('montant') - montant)
            else:
                return JsonResponse({'status': 0, 'message': 'inssuffisance du capitale'})
        if montant1:
            Wallet.objects.filter(user=user).update(montant=F('montant') + montant1)
        return JsonResponse({'status': 1, 'message': 'success!!'})


class ProfileUpdateView(APIView):
    def get_object(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except:
            return None
            
    def get(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = Profile.objects.get(user=pk)
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            print(tokenview)
            user = Profile.objects.get(user=tokenview)
        if not user:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})

        # You have a serializer that you specified which fields should be available in fo
        serializer = ProfileSerializer(user)
        # And here we send it those fields to our react component as json
        # Check this json data on React side, parse it, render it as form.
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = User.objects.get(pk=pk)
            userProfile = Profile.objects.get(pk=pk)
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            user = User.objects.get(pk=tokenview)
            userProfile = Profile.objects.get(pk=tokenview)
            
        username = request.data.get("username", None)
        first_name = request.data.get("first_name", None)
        last_name = request.data.get("last_name", None)
        email = request.data.get("email", None)
        phone = request.data.get("phone", None)
        bio = request.data.get("bio", None)
        photo = request.data.get("photo", None)
        if username:
            fil = User.objects.filter(username=username)
            if not fil:
                if username:
                    user.username = username
                if email:
                    user.email = email
                if first_name:
                    user.first_name = first_name
                if last_name:
                    user.last_name = last_name
                if phone:
                    userProfile.phone = phone
                if bio:
                    userProfile.bio = bio
                if photo:
                    userProfile.photo = photo
                user.save()
                userProfile.save()
                return JsonResponse({'status': 1, 'message': 'Your profile updated successfully!'})
            else:
                return JsonResponse({'status': 0, 'message': 'username existe deja'})
        else:
            if username:
                user.username = username
            if email:
                user.email = email
            if first_name:
                user.first_name = first_name
            if last_name:
                user.last_name = last_name
            if phone:
                userProfile.phone = phone
            if bio:
                userProfile.bio = bio
            if photo:
                userProfile.photo = photo
            user.save()
            userProfile.save()
            return JsonResponse({'status': 1, 'message': 'Your profile updated successfully!'})
            
class RetraitView(APIView):
    def get(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = Wallet.objects.get(user=pk)
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            user = Retrait.objects.get(user=tokenview)
        if not user:
            return JsonResponse({'status': 0, 'message': 'User with this id not found'})

        # You have a serializer that you specified which fields should be available in fo
        serializer = RetraitSerializer(user, many=True)
        # And here we send it those fields to our react component as json
        # Check this json data on React side, parse it, render it as form.
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format=None):
        pk = request.GET.get('pk', None)
        if pk != None:
            user = User.objects.get(pk=pk)
        else:
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            user = User.objects.get(pk=tokenview)
        montant = request.data.get("montant")
        moncash_numero = request.data.get("phone")
        Retrait.objects.create(user=user, montant=montant)
        Wallet.objects.filter(user=user).update(montant=F('montant') - montant)
        subject = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        messageadmin = "L'utilisateur %s veut faire un retrait de (%s Gourdes) a son compte moncash (%s) \n veuillez etre sure apres chaque retrait envoyer \n que vous activerez le button envoyer en True" % (user.username, montant, moncash_numero)
        mail_admins(subject, messageadmin)
        return JsonResponse({'status': 1, 'message': 'wallet success'})

class QuestionView(APIView):
    def get(self, request, format=None):
        quizz_id = request.GET.get('quizz_id')
        pk = request.GET.get('pk', None)
        if pk != None:
            ques = questions.objects.filter(quizz_id=quizz_id, is_live=True).order_by('?')
        else:
            # token = request.META.get('HTTP_AUTHORIZATION', '')
            token = request.META.get('HTTP_AUTHORIZATION', '').split()
            key = token[1].lower()[0:8]
            tokenview = get_object_or_404(AuthToken, token_key=key).user.id
            # tokenview = AuthToken.objects.get(token_key=key).user
            ques = questions.objects.filter(quizz_id=quizz_id).order_by('?')
        if not ques:
            return JsonResponse({'status': 0, 'message': 'no question fund'})

        # You have a serializer that you specified which fields should be available in fo
        serializer = QuestionSerializer(ques, many=True)
        # And here we send it those fields to our react component as json
        # Check this json data on React side, parse it, render it as form.
        return JsonResponse(serializer.data, safe=False)