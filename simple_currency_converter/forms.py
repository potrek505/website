from django import forms

CURRENCY_CHOICES = [
    ('THB', 'Thai Baht'),
    ('USD', 'US Dollar'),
    ('AUD', 'Australian Dollar'),
    ('HKD', 'Hong Kong Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('NZD', 'New Zealand Dollar'),
    ('SGD', 'Singapore Dollar'),
    ('EUR', 'Euro'),
    ('HUF', 'Hungarian Forint'),
    ('CHF', 'Swiss Franc'),
    ('GBP', 'British Pound'),
    ('UAH', 'Ukrainian Hryvnia'),
    ('JPY', 'Japanese Yen'),
    ('CZK', 'Czech Koruna'),
    ('DKK', 'Danish Krone'),
    ('ISK', 'Icelandic Krona'),
    ('NOK', 'Norwegian Krone'),
    ('SEK', 'Swedish Krona'),
    ('RON', 'Romanian Leu'),
    ('BGN', 'Bulgarian Lev'),
    ('TRY', 'Turkish Lira'),
    ('ILS', 'Israeli Shekel'),
    ('CLP', 'Chilean Peso'),
    ('PHP', 'Philippine Peso'),
    ('MXN', 'Mexican Peso'),
    ('ZAR', 'South African Rand'),
    ('BRL', 'Brazilian Real'),
    ('MYR', 'Malaysian Ringgit'),
    ('IDR', 'Indonesian Rupiah'),
    ('INR', 'Indian Rupee'),
    ('KRW', 'South Korean Won'),
    ('CNY', 'Chinese Yuan'),
    ('XDR', 'IMF SDR'),
]

class CurrencyConverterForm(forms.Form):
    amount = forms.DecimalField(label='Amount in PLN', decimal_places=2)
    currencies = forms.MultipleChoiceField(
        choices=CURRENCY_CHOICES,
        widget=forms.CheckboxSelectMultiple,
        label='Select Currencies'
    )
