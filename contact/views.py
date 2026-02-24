from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return redirect('contact')

    return render(request, "contact/contact.html")