
from .models import Person, Patient, Doctor
# -----already present functions to use --------------
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

def signup(request):
    print('inside signup')
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        profile_picture = request.FILES.get('profile_picture')  # Assuming you're using enctype="multipart/form-data" in your HTML form
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        address_line1 = request.POST.get('address_line1')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        user_type = request.POST.get('user_type')

        # Check if the username already exists
        if Person.objects.filter(username=username).exists():
            print('Username already exists!')
            # Handle the error or redirect as needed
            return redirect('signup')

        # Hash the password
        hashed_password = make_password(password)
        print('hash pass',hashed_password)

        # Create a new Person instance
        user = Person.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_password,
            profile_picture = profile_picture,

            address_line1=address_line1,
            city=city,
            state=state,
            pincode=pincode,
            user_type = user_type
        )

        # Save the user instance
        user.save()
        user1 = User.objects.filter(username = username)
            
        user1 = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=hashed_password,
          
        )
        user1.save()
        if user_type == 'patient':
            print('i am patient')
            Patient.objects.create(user=user)
        elif user_type == 'doctor':
            print('i am doctor')
            Doctor.objects.create(user=user)

        return redirect('login')  # Redirect to the login page or wherever needed

    return render(request, 'signup.html')




def user_login(request):
    if request.method == "POST":
        password = request.POST.get('password')
        username = request.POST.get('username')
        check_u =  User.objects.filter(username=username).first()
        
        if check_u is None:
            print('user not found')
            # messages.error(request, 'Invalid Credentials!')
            return redirect('login')
        
        check_p = check_password(password, check_u.password)
        
        if not check_p:
            print('password is incorrect')
            # messages.error(request, 'Invalid Credentials!')
            return redirect('login')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
    
    return render(request, 'login.html')



def dashboard(request):
    print('inside dashboard')
    print("REQUEST : ",request)
    # user = User.objects.get(username)
    print("from request : ",request.user.username)
    u = request.user.username
   
    
    mydata = Person.objects.filter(username=u).first()
    print(mydata)
    print(mydata.email)
    print(mydata.profile_picture)
    print(mydata.profile_picture.url)
    context = {
        'username': mydata.username,
        'profile_picture': mydata.profile_picture,
        'first_name': mydata.first_name,
        'last_name': mydata.last_name,
        'email': mydata.email,
        'city': mydata.city,
        'state': mydata.state,
        'address_line1': mydata.address_line1
    }
    
    print("my data : ", context)

    return render(request, 'dashboard.html',context)


    
    
