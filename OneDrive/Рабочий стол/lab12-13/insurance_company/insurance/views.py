from django.shortcuts import render, get_object_or_404, redirect
from .models import Client, Policy

def home(request):
    clients = Client.objects.all()
    return render(request, 'insurance/home.html', {'clients': clients})

def add_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        Client.objects.create(name=name, email=email, phone=phone)
        return redirect('home')
    return render(request, 'insurance/add_client.html')

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'insurance/client_detail.html', {'client': client})