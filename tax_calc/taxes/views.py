from django.shortcuts import render, redirect
from .models import CarouselImages, TaxSavingsGuide, TaxSlabRates,TaxDetails,UserDetails
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def index_requestView(request):
    data = CarouselImages.objects.all()
    guide = TaxSavingsGuide.objects.all()
    slab_rates = TaxSlabRates.objects.all()
    
    if request.method == 'POST':
        financial_year = request.POST.get('financial_year')
        age_group = request.POST.get('age_group')
        category = request.POST.get('category')
        old_regime = request.POST.get('old_regime')
        new_regime = request.POST.get('new_regime')
        
        income = eval(request.POST.get('income'))
        other_income = eval(request.POST.get('other_income'))
        total_tax = income + other_income
        print(total_tax)
        
        std_deduction = eval(request.POST.get('std_deduction'))
        ded_80c = eval(request.POST.get('ded_80c'))
        pro_tax = eval(request.POST.get('pro_tax'))
        nps = eval(request.POST.get('nps'))
        hra = eval(request.POST.get('hra'))
        home_loan = eval(request.POST.get('home_loan'))
        total_deduction = std_deduction + ded_80c + pro_tax + nps + home_loan + hra
        print(total_deduction)
        
        taxable_income = eval(request.POST.get('taxable_income'))
        tax_on_taxable = eval(request.POST.get('tax_on_taxable'))
        tax_rebate = eval(request.POST.get('tax_rebate'))

        TaxDetails(financial_year=financial_year, age_group=age_group, category_emp_or_pen=category,).save()
    
    
    context= {"data": data,
            "guide": guide,
            "slab_rates": slab_rates,}
    
    #return redirect("/index")

    return render(
        request,
        "taxes/index.html",
        context
    )


def login_requestView(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        signin = UserDetails.objects.filter(username=username, password=password)
        if signin:
            a = UserDetails.objects.get(username=username, password=password)
            uid = a.user_id
            username = a.username
            request.session['id'] = uid
            request.session['username'] = username
            return redirect("http://127.0.0.1:8000")
        else:
            return redirect("/login")
    return render(request, "taxes/login.html")


def base_requestView(request):
    return render(request, "taxes/base.html")


def register_requestView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        zipcode = request.POST.get('zipcode')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass2 == pass1:
            UserDetails(name=name, password=pass1, email=email, zipcode=zipcode).save()
            return redirect("/")
        else:
            return redirect("/register")

    else:
        return render(request, 'taxes/register.html')


def logout_requestView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')

def saved_recordsl_requestView(request):
    return render(request, "taxes/saved_records.html")