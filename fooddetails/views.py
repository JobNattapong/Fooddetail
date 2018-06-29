from django.shortcuts import redirect, render
from django.http import HttpResponse
from fooddetails.models import Food

# Create your views here.
def homepage(request):
    error_message = ""
    data_food = Food.objects.all()
    return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'error_message' : error_message})

def add_food(request):
    error_message = ""
    data_food = Food.objects.all()
    food_ = str(request.POST['nameFood'])
    sugar_ = request.POST['sizeSugar']
    protein_ = request.POST['sizeProtein']
    if (food_ != '' and sugar_ != '' and protein_ != ''):
        Food.objects.create(food_text = food_ ,sugar = sugar_ ,protein = protein_)
        return redirect('/')
    else:
        error_message = "please enter fully"
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'error_message' : error_message})

def delete_row_table(request):
    del_id = int(request.POST['del_id'])
    Food.objects.get(id=del_id).delete()
    return redirect('/')
