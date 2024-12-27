from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login

# Create your views here.

def home(request):
    return render (request, 'home.html')

def user_login(request):   
    #if method POST
    if request.method == 'POST':
    #extract username and password from form data
        username = request.POST.get('username')
        password = request.POST.get('password')        
        #authenticate user
        
        user = authenticate(username = username, password = password)
        
        #if user
        if user is not None:
            login(request,user)
            return redirect('dashboard')
            #correct - dashboard.html
            
        #else - login.html
        else:
            return redirect("login") 
    
    return render (request, 'login.html')

def user_signup(request):
    # Step 1: Check if the request method is POST (form submission)
        
        # Step 2: Extract the form data (username, email, password, password confirmation)
        # - Get username from the form data
        # - Get email from the form data
        # - Get password1 from the form data (password entered by the user)
        # - Get password2 from the form data (password confirmation entered by the user)

        # Step 3: Validate the extracted data
        # - Check if password1 matches password2
        # - If passwords do not match, return an error message
        
        # Step 4: Check if the username already exists in the database
        # - Query the database for an existing user with the same username
        # - If a user with the same username exists, return an error message

        # Step 5: Create a new user in the database
        # - If all validations pass, create a new user with the extracted details (username, email, password)
        
        # Step 6: Redirect the user after successful signup
        # - Redirect the user to a different page (e.g., dashboard) after successful signup
        
        # Step 7: Redirect the user after unsuccessful signup
        # - Redirect the user to a signup page
        
    # Step 9: If the request method is not POST (i.e., it's a GET request), render the signup form
    # - This is where the form is displayed when the page is first loaded or when errors occur
    return render(request, 'signup.html')


def dashboard(request):
    return render (request, 'dashboard.html')