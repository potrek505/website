from django.shortcuts import render
from .forms import CurrencyConverterForm
from .backend import exchange_rates

def currency_converter(request):
    results = None
    if request.method == 'POST':
        form = CurrencyConverterForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            selected_currencies = form.cleaned_data['currencies']
            results = exchange_rates(amount, selected_currencies)

    else:
        form = CurrencyConverterForm()

    return render(request, 'simple_currency_converter.html', {'form': form, 'results': results})
