from django.shortcuts import render, redirect
from .models import CarouselImages, TaxSavingsGuide, TaxSlabRates,TaxDetails,UserDetails,UserFeedback
from django.views.generic.base import View
from django.contrib import messages
from django.contrib.auth import logout

# Create your views here.
def login_requestView(request):
    if request.POST:
        name = request.POST['name']
        password = request.POST['password']
        signin = UserDetails.objects.filter(name=name, password=password)
        if signin:
            a = UserDetails.objects.get(name=name, password=password)
            uid = a.user_id
            name = a.name
            request.session['id'] = uid
            request.session['name'] = name
            return redirect("http://127.0.0.1:8000")
        else:
            return redirect("/login")
    return render(request, "taxes/login.html")


def index_requestView(request):
    guide = TaxSavingsGuide.objects.all()
    slab_rates = TaxSlabRates.objects.all()
    id = request.session['id']
    name = request.session['name']
    
    if request.method == 'POST':
        u_name = request.session['name']
        name = UserDetails.objects.get(name=u_name)
        financial_year = request.POST.get('Financial_year')
        age_group = request.POST.get('Age_group')
        category = request.POST.get('Category')
        old_regime = request.POST.get('Regimes')
        new_regime = request.POST.get('Regimes')
        
        income = request.POST.get('Income')
        other_income = request.POST.get('Other_income')
        total_tax = request.POST.get('Total_tax')
        
        std_deduction = request.POST.get('Std_deduction')
        ded_80c = request.POST.get('Ded_80c')
        pro_tax = request.POST.get('Pro_tax')
        nps = request.POST.get('Nps')
        hra = request.POST.get('Hra')
        home_loan = request.POST.get('Home_loan')
        tax_rebate =request.POST.get('Tax_rebate')
        surcharge =request.POST.get('Surcharge')
        education_cess =request.POST.get('Education_cess')
        
        taxable_income = request.POST.get('Taxable_income')
        tax_on_taxable = request.POST.get('Tax_on_taxable')
        tax_rebate = request.POST.get('Tax_rebate')
        
        
        TaxDetails(name=name,financial_year=financial_year, age_group=age_group, category_emp_or_pen=category,
                   regime= old_regime or new_regime,salary_income=income,other_income=other_income,
                    standard_deduction=std_deduction,professional_tax=pro_tax,
                   house_rent_exemption=hra,home_loan=home_loan,deductions_u_80c=ded_80c,nps_u_80c=nps,
                   taxable_income=taxable_income,tax_on_taxable_income=tax_on_taxable,rebate_u_87a=tax_rebate,
                   surcharge_on_tax=surcharge,education_cess=education_cess,total_tax=total_tax).save()
        return redirect("/",{"guide": guide,
            "slab_rates": slab_rates,
            "name":name,"id":id})
    
    else:
        return render(
            request,
            "taxes/index.html",
            {"guide": guide,
            "slab_rates": slab_rates,
            "name":name}
        ) 
        
    
def feedback_requestView(request):
    if request.method == 'POST':
        u_name = request.session['name']
        name = UserDetails.objects.get(name=u_name)
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        UserFeedback(name=name,email=email,description=message).save()
        return redirect("/")
    else:
        return render(
            request,
            "taxes/feedback.html"  
        ) 

def del_records_requestView(request):
    name = request.session.update('name')
    records = TaxDetails.objects.get(name=name)
    records.delete()
    return redirect('/home')

def base_requestView(request):
    return render(request, "taxes/base.html")


def register_requestView(request):
    data = CarouselImages.objects.all()
    context= {"data": data}
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        zipcode = request.POST.get('zipcode')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass2 == pass1:
            UserDetails(name=name,password=pass1,email=email, zipcode=zipcode).save()
            return redirect("/login")
        else:
            return redirect("/register")
    else:
        return render(request, 'taxes/register.html',context)


def logout_requestView(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/login')

def saved_recordsl_requestView(request):
    name = request.session['name']
    id = request.session['id']
    saved_records = TaxDetails.objects.all()
    context = {"saved_records":saved_records}
    
    return render(request, "taxes/saved_records.html",context)