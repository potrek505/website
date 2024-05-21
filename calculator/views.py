from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .backend import profit

def calculator(request):
    result = None  # Inicjalizuj wynik jako None, aby obsłużyć GET i inne żądania
    if request.method == 'POST':
        try:
            capital_in_pln = float(request.POST.get('PLN', 0))
            deposit_fee = float(request.POST.get('deposit_fee', 0))
            p2p_price = float(request.POST.get('p2p_price', 0))
            result = str(profit(capital_in_pln, deposit_fee, p2p_price))
        except (ValueError, TypeError):
            result = 'Invalid input. Please enter valid numbers.'
    return render(request, 'calculator.html', {'result': result})