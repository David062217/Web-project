from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.

def contact (request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(data = request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            content = request.POST.get("content")

            email = EmailMessage("Nuevo mensaje", 
            "The person named {} with the email {} has written a message \n\n {}".format(name,email,content),"", ["monterokdavid@gmail.com"], reply_to= [email])

            try:
                email.send()
                return redirect("/contact/?valid")
            except:
                return redirect("/contact/?error")
                
    return render(request,'app_contact/contact.html', {'myForm': form}) 