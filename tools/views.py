import os
from django.shortcuts import render
import re
from cryptography.fernet import Fernet
from django.contrib.auth.forms import UserCreationForm
from tools.models import PasswordEntry
from django.contrib.auth.hashers import make_password


# Encryption setup
key = Fernet.generate_key()
cipher_suite = Fernet(key)

from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from .models import PasswordEntry
import re  # Import regex for password strength checking

def password_checker(request):
    if request.method == "POST":
        password = request.POST.get('password')
        
        # Hash the password
        hashed_password = make_password(password)

        # Save the hashed password to the database
        password_entry = PasswordEntry(hashed_password=hashed_password)
        password_entry.save()
       


        # Check password strength
        strength_message = check_password_strength(password)

        return render(request, 'password_checker.html', {
            'strength_message': strength_message,
        })

    return render(request, 'password_checker.html')

def home(request):
    return render(request, 'home.html')

def check_password_strength(password):
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters."
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase letter."
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase letter."
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one number."
    if not re.search(r'[!@#\$%\^&\*]', password):
        return "Weak: Password should contain at least one special character."
    
    return "Strong Password!"

# Network Scanner
def network_scanner(request):
    result = None
    if request.method == 'POST':
        ip_range = request.POST.get('ip_range')
        result = scan_network(ip_range)
    
    return render(request, 'network_scanner.html', {'result': result})

def scan_network(ip_range):
    active_ips = []
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        response = os.system(f"ping -c 1 {ip}")
        if response == 0:
            active_ips.append(ip)
    
    if active_ips:
        return f"Active devices found: {', '.join(active_ips)}"
    return "No active devices found in the range."

# Encryption/Decryption Tool
def encryption_tool(request):
    encrypted_message = None
    decrypted_message = None

    if request.method == 'POST':
        message = request.POST.get('message')
        action = request.POST.get('action')
        
        if action == 'encrypt':
            encrypted_message = cipher_suite.encrypt(message.encode()).decode()
        elif action == 'decrypt':
            decrypted_message = cipher_suite.decrypt(message.encode()).decode()

    return render(request, 'encryption_tool.html', {
        'encrypted_message': encrypted_message,
        'decrypted_message': decrypted_message
    })




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login page after registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})