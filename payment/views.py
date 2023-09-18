from django.shortcuts import render

# Create your views here.
def view_payment(request):

    """ A view that renders payment content page. """
    return render(request, 'payment/payment.html')