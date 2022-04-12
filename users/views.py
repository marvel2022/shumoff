from django.urls import  reverse_lazy
from django.views.generic import CreateView
# from django.contrib.auth.forms import UserCreationForm


from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponse, Http404, HttpResponseRedirect ,BadHeaderError
from django.views import View

# from django.contrib.auth.forms import  AuthenticationForm  # Now we can use 'LoginForm' instead of 'AuthenticationForm'
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import FeedbackForm
from django.core.mail import send_mail
from django.conf import settings
# from shumoff import settings

from .forms import NewUserForm
from core.models  import Category
# Create your views here.


class NewUserCreationForm(CreateView):
    template_name = 'registration/register.html'
    form_class = NewUserForm
    success_url = reverse_lazy('login')

def logout(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("Products:product-list")


class Contact(View):
    template_name ='contact.html'
    context       = {}
    def get(self, request, *args, **kwargs):
        category_list = Category.objects.all()
        self.context["category_list"] = category_list
        return render(
            request,
            self.template_name,
            self.context
        )

class Message(View):
    template_name ='messageform.html'
    context       = {}

    def get(self, request, *args, **kwargs):
        form                 = FeedbackForm()
        category_list = Category.objects.all()

        self.context["category_list"] = category_list
        self.context['form'] = form
        
        return render(
            request,
            self.template_name,
            self.context
        )
    
    def post(self, request, *args, **kwargs):
        category_list = Category.objects.all()

        if request.method == "POST":
            form = FeedbackForm(request.POST)
            if form.is_valid():
                first_name   = form.cleaned_data['name']
                email        = form.cleaned_data['email']
                phone_number = form.cleaned_data['phone']
                text         = form.cleaned_data['text']

                try:
                    subject    = "FULFIL EDUCATION"
                    thoughts   = f"{first_name} dan yangi xabar: \n\n{text}\nTel: {phone_number}\nEmail: {email}"
                    sender     = settings.EMAIL_HOST_USER
                    recipients = ['dovurovjamshid95@gmail.com']
                    # recipients = ['dovurovjamshid95@gmail.com']

                    send_mail(subject, thoughts, sender, recipients, fail_silently=False)
                      
                    messages.success(request, f"{first_name} xabaringiz muvofaqiyatli yuborildi.")
                except BadHeaderError:
                    return HttpResponse('Invalid header')
                return redirect('User:message')
            else:
                for msg in form.errors:
                    messages.error(request, f"{msg}")
                return redirect('User:message')
        self.context = {
            'form': form,
            "category_list": category_list,
        }
        
        return render(
            request, 
            self.template_name,
            self.context
        )