from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Home Page View
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

# Reservation View
def reservations(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        date = request.POST.get('date')
        time = request.POST.get('time')
        phone = request.POST.get('phone')
        people = request.POST.get('people')
        message = request.POST.get('message')

        age = request.POST.get('age')
        prefer = request.POST.get('prefer')
        role = request.POST.get('role')
        comment = request.POST.get('comment')
        purpose = request.POST.get('purpose')

        from .models import table
        
        reservation = table(
            name=name,
            email=email,
            date=date,
            time=time,
            phone=phone,
            people=people,
            message=message,
            age=age,
            prefer=prefer,
            role=role,
            comment=comment,
            purpose=purpose
        )

        reservation.save()
        messages.success(request, "Your table has been booked successfully!")
        return redirect('reservations')

    return render(request, 'reservations.html')

    

# Contact View
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Import the 'booking' model here to avoid circular import
        from .models import booking
        
        # Ensure to import the 'booking' model if it's used
        contact = booking(name=name, email=email, subject=subject, message=message)
        contact.save()

        # Send a confirmation message
        messages.success(request, "Your message has been sent successfully!")

    return render(request, 'contact.html')

# Gallery Page
def gallery(request):
    return render(request, 'gallery.html')

# Handle Signup
def handleSignup(request):
    if request.method == 'POST':
        # Get the post parameters
        username = request.POST['username']
        fname = request.POST['fname1']
        lname = request.POST['lname1']
        email = request.POST['email1']
        password1 = request.POST['password2']
        password2 = request.POST['password4']

        # Form validation
        if len(username) > 10:
            messages.error(request, "Username must be under 10 characters")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "Username must contain letters and numbers only")
            return redirect('home')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('home')

        # Create new user
        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been created successfully")
        return redirect('home')

    return HttpResponse('404 not found')

# Handle Login
def handlelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password6']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")

    return HttpResponse('404 not found')

# Handle Logout
def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('home')
