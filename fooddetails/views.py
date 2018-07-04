from django.shortcuts import render
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
    sugar_ = request.POST['volumeSugar']
    protein_ = request.POST['volumeProtein']
    if (food_ != '' and sugar_ != '' and protein_ != ''):
        Food.objects.create(food_text = food_ ,sugar = sugar_ ,protein = protein_)
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'error_message' : error_message})
    else:
        error_message = "please enter completely"
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'error_message' : error_message})

def delete_row_table(request):
    delete_error = ''
    data_food = Food.objects.all()
    delete_food = request.POST['food_del']
    if (delete_food != ''):
        food = Food.objects.filter(food_text=delete_food)
        food.delete()
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'delete_error' : delete_error})
    else:
        delete_error = "Incomplete!!!!!"
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'delete_error' : delete_error})

def edit_food(request):
    edit_error = ''
    data_food = Food.objects.all()
    Oldfood = request.POST['old_name_food']
    Newfood = request.POST['new_name_food']
    Newsugar = request.POST['new_name_sugar']
    Newprotein = request.POST['new_name_protein']

    if (Oldfood != '' and Newfood != '' and Newsugar != '' and Newprotein != ''):
        fooddetail = Food.objects.get(food_text=Oldfood)
        fooddetail.food_text = Newfood
        fooddetail.sugar = Newsugar
        fooddetail.protein = Newprotein
        fooddetail.save()
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'edit_error' : edit_error})
    else:
        edit_error = "Incomplete!!!!!"
        return render(request, 'fooddetails/homepage.html', {'foods' : data_food, 'edit_error' : edit_error})
