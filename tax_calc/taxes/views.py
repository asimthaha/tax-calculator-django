from django.shortcuts import render
from .models import CarouselImages, TaxSavingsGuide, TaxSlabRates


# Create your views here.
def index(request):
    data = CarouselImages.objects.all()
    guide = TaxSavingsGuide.objects.all()
    slab_rates = TaxSlabRates.objects.all()
    return render(
        request,
        "taxes/index.html",
        {
            "data": data,
            "guide": guide,
            "slab_rates": slab_rates,
        },
    )


def login_request(request):
    return render(request, "taxes/login.html")


def baseView(request):
    return render(request, "taxes/base.html")


def register_request(request):
    return render(request, "taxes/register.html")
