
from email import message
from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from  django.contrib import messages
from django.contrib import auth

# Create your views here.


def home(request) :

    if not request.user.is_authenticated: return redirect('user_login')

    return render(request ,'registration/home.html' )    
    
def user_login(request):

    message = None

    if request.method  == 'POST' :

        username=request.POST['username']
        password=request.POST['password']

        # username=request.POST.get('username')
        
        user = authenticate(username=username, password=password)
        
        if user is not None : 

            login(request, user)
            return redirect('home')  

        else:

            message = 'نام کاربری یا رمز عبور اشتباه است'
            return render(request, 'registration/login_home.html', {'message':message})


    return render(request, 'registration/login_home.html')




def signUp (request):
    if request.method =="POST" :
        #user = authenticate(username=request.POST['username'], password=request.POST['password'])
        username=request.POST['username']
        password=request.POST['password']
        confirm_password = request.POST['confirm_password']

        print( username , password ,confirm_password)
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'این نام کاربری قبلا ثبت شده است')
                return redirect(request , 'home')
        
            else:
                user = User.objects.create_user(username=username, password=password )
                                       
                user.save()
                
                return redirect("home")


        else:
            messages.info(request, 'تکرار رمزعبور مطابقت ندارد')
            return redirect(request,'signUp')
            

    else:
        return render(request, 'registration/signUp.html')



def logout_user(request):
    logout(request)
    return redirect('user_login')


