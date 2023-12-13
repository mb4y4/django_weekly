from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Food
from .forms import FoodForm

# Create your views here.
# def index(request):
#     return render(request, 'index.html')

@login_required
def food_list(request):
    foods = Food.objects.filter(user=request.user)
    return render(request, 'index.html', {'foods': foods})

@login_required
def add_food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            Food = form.save(commit=False)
            Food.user = request.user
            Food.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'add_food.html', {'form': form})