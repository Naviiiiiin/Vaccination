from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required  
from .forms import AppointmentForm 
from .models import Appointment, Area, Hospitals
from django.template.loader import render_to_string
from django.core.mail import send_mail
import secrets
from .models import Profile

@login_required
def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()

          
            subject = 'Appointment Confirmation'
            message = render_to_string('appointment_confirmation_email.html', {'appointment': appointment})
            from_email = 'navinvy549@gmail.com'
            to_email = [request.user.email]

            send_mail(subject, message, from_email, to_email, html_message=message)

            messages.success(request, 'Appointment booked successfully!')
        
            return redirect('appointment_details', appointment_id=appointment.pk)

    else:
        form = AppointmentForm()
        form_errors = None
    
    area_data = Area.objects.all()
    hospital_data = Hospitals.objects.all()

    return render(request, 'book_appointment.html', {'form': form, 'area_data': area_data, 'hospital_data': hospital_data})



def index(request):
   
    
    return render(request, 'index.html',)

def about(request):
    
    return render(request, 'about.html') 

def contact(request):
   
    return render(request, 'contact.html') 


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'register.html')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'email already exist')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            user.save()
            # subject = 'Aboout Registration'
            # messages = f'HI {username}.this is your appointment'
            # email_from = 'navinvy549@gmail.com'
            # rec_list = [email,]
            # send_mail(subject, messages, email_from, rec_list ) 
            return redirect('login')
    
    return render(request, 'register.html')


# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         try:
#             user = User.objects.get(username=username)
#         except User.DoesNotExist:
#             messages.error(request, 'User does not exist. Please register first.')
#             return render(request, 'login.html')

#         user = authenticate(username=username, password=password)
#         if user is not None:
#             login(request, user)
        
#             return redirect('index')
#         else:
#             messages.error(request, 'Invalid username or password')

#     return render(request, 'login.html')



def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'login.html')


def appointment_details(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)         
    return render(request, 'appointment_details.html', {'appointment': appointment})



def forgot_password(request):
    if request.method == 'POST': 
        email = request.POST.get('email')
        print(f"Password reset link sent to {email}")
        return redirect('password_reset_confirmation')  
    else:
       
        return render(request, 'forgot_password.html')  

def generate_verification_code():
    return f"{secrets.randbelow(1000000):06}"


def verification_email(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'No user found with this email address.')
            return redirect('forgot_password')

       
        profile, created = Profile.objects.get_or_create(user=user)
        verification_code = generate_verification_code()
        profile.verification_code = verification_code
        profile.save()

        
        subject = 'Password Reset Verification Code'
        message = render_to_string('verification_email.html', {'verification_code': verification_code})
        from_email = 'navinvy549@gmail.com'
        to_email = [email]  
        send_mail(subject, message, from_email, to_email, html_message=message)

        
        return redirect('verify_reset_code')

    return render(request, 'forgot_password.html')



def verify_reset_code(request):
    if request.method == 'POST':
        verification_code = request.POST.get('verification_code')
        email = request.POST.get('email')

        try:
          
            user = User.objects.get(email=email)

           
            if hasattr(user, 'profile'):
               
                if user.profile.verification_code == verification_code:
                    
                    return render(request, 'login.html', {'email': email})
                else:
                    messages.error(request, 'Invalid verification code. Please try again.')
            else:
                messages.error(request, 'User has no profile.')

        except User.DoesNotExist:
            messages.error(request, 'User does not exist.')

    return render(request, 'verification_code.html')




def reset_password(request, email):
    user = get_object_or_404(User, email=email)

    if request.method == 'POST':
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            # Set the new password
            user.set_password(new_password)
            user.save()

            messages.success(request, 'Password reset successfully. You can now log in with your new password.')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')

    return render(request, 'reset_password.html', {'email': email})
