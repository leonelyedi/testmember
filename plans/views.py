from django.shortcuts import render, get_object_or_404, redirect
from .forms import CustomSignupForm
from django.urls import reverse_lazy
from django.views import generic
from .models import Fitness
from django.contrib.auth import authenticate, login

from django.contrib.auth.decorators import login_required, user_passes_test
import stripe
from django.http import HttpResponse

stripe.api_key = 'pk_test_51OEPwAKVdMVSZMCf8Skqp4fWVNDZg6fEO6ZsuPdiGB9i4wJse3vt2ENOkeX2JgARuSmK82DNlsi51Sf1C6USXeRr00LBrqgfGZ'
# https://www.youtube.com/watch?v=lCTdgXfIkqA 
def home(request):
    plans = Fitness.objects
    return render(request, 'plans/home.html', {'plans': plans})


def plan(request, pk):
    plan = get_object_or_404(Fitness, pk=pk)
    if plan.premium:
        return redirect('join')
    else:
        return render(request, 'plans/plan.html', {'plan': plan})


def join(request):
    return render(request, 'plans/join.html')

def form(request):
    return render(request, 'plans/form.html')

def checkout(request):
    return render(request, 'plans/checkout.html')


def settings(request):
    return render(request, 'registration/settings.html')


class SignUp(generic.CreateView):
    form_class = CustomSignupForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        valid = super(SignUp, self).form_valid(form)
        username, password = form.cleaned_data.get(
            'username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid
