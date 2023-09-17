from django.shortcuts import render
from . models import Charity

# Create your views here.
def all_organizations(request):

    """ A view to show all the charity organization to donate to """
    charities = Charity.objects.all()
    context = {
        'charities':charities,
    }
    return render(request, 'charity_hub/charities.html', context)
  

