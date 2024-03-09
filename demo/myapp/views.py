from django.shortcuts import render, redirect
from .models import TodoItem
from .forms import CustomerForm
from .models import Customer
from datetime import datetime
from .models import News

def home(request):
    return render(request,"home.html")

def contact(request):
    return render(request, "contact.html")


def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items })


def book(request):
    form = CustomerForm()

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Hämta bokningsdatum och tid från formuläret
            booking_date = form.cleaned_data['booking_date']
            booking_time = form.cleaned_data['booking_time']

            # Kontrollera om det redan finns en bokning för det angivna datumet och tiden
            existing_booking = Customer.objects.filter(booking_date=booking_date, booking_time=booking_time).exists()

            if not existing_booking:
                # Ingen dubbelbokning, spara bokningen
                form.save()
                return redirect('todos')
            else:
                # Dubbelbokning, visa felmeddelande eller hantera på lämpligt sätt
                form.add_error(None, "This date and time is already booked.")
                # Återvänd inte här, låt användaren rätta till felet och skicka in formuläret igen
    time_slots = [f"{i:02d}" for i in range(0, 61, 15)]

    context = {'form': form}
    return render(request, "book.html", context)


def news_list(request):
    news_list = News.objects.all()
    return render(request, 'news_list.html', {'news_list': news_list})


def home(request):
    news_list = News.objects.all().order_by('-created_at')[:5]  
    return render(request, 'home.html', {'news_list': news_list})


