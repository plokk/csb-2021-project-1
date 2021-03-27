from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader

from .models import CreditCard, Exercise, User

@login_required
def add(request):
    if request.method == 'POST':
        description = request.POST.get('description').strip()
        exercise = Exercise.objects.create(owner=request.user, description=description)
    return redirect('/profile/%s' % request.user.id)

@login_required
def add_credit_card(request):
    if request.method == 'POST':
        number = request.POST.get('credit-card-number').strip()
        name = request.POST.get('credit-card-holder-name').strip()
        csv = request.POST.get('credit-card-csv').strip()
        credit_card = CreditCard.objects.create(owner=request.user, number=number, name=name, csv=csv)
    return redirect('/profile/%s' % request.user.id)

@login_required()
def index(request):
    exercises = Exercise.objects.order_by('-date')[:5]
    context = {'exercises': exercises}
    return render(request, 'exercises/index.html', context)

@login_required()
def profile(request, user_id):
    try:
        profile_user = User.objects.get(id=user_id)
        exercises = Exercise.objects.filter(owner=profile_user).order_by('-date')
        credit_cards = CreditCard.objects.filter(owner=profile_user)
        is_me = profile_user == request.user
        context = {'credit_cards': credit_cards, 'exercises': exercises, 'is_me': is_me, 'profile_user': profile_user}
        return render(request, 'profile/index.html', context)
    except  User.DoesNotExist:
        return redirect('/')
