from django.contrib.auth import authenticate, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def sign_in(request):
    if request.method == 'POST':
        print(request)
        email = request.data.get('email')
        pwd = request.data.get('pswd')
        user = authenticate(email=email, password=pwd)
        print(user, email, pwd)
        if user is not None:
            token = Token.objects.filter(user=user)
            if token:
                token[0].delete()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': token.key}, status=200)
        else:
            return JsonResponse({'error': 'wrong phone or password'}, status=403)

@api_view(['GET'])
def log_out(request):
    if request.method == 'GET':
        user = request.user
        t = Token.objects.get(user=user).delete()
        logout(request)
        return JsonResponse({'done': 'logout'}, status=200)