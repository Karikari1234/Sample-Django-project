from django.shortcuts import render
from MyAppTwo.models import User

# Create your views here.


def index(request):
    return render(request, 'MyAppTwo/index.html')


def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users': user_list}
    return render(request, "MyAppTwo/users.html", context=user_dict)
