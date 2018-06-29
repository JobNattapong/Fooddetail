from django.shortcuts import redirect, render
from django.http import HttpResponse
from fooddetails.models import Food

# Create your views here.
def homepage(request):
    data_food = Food.objects.all()
    return render(request, 'fooddetails/homepage.html', {'foods' : data_food})

def add_food(request):
    Food.objects.create(
    food_text = request.POST['nameFood'],
    sugar = int(request.POST['sizeProtein']),
    protein = int(request.POST['sizeSugar']),
        )
    return redirect('/')

def delete_row_table(request):
    del_id = int(request.POST['del_id'])
    Food.objects.get(id=del_id).delete()
    return redirect('/')
