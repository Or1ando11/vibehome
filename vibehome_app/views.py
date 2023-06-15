from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import ContactForm
from .models import ContactMessage, Estate
import requests

#strona glowna
def index(request):
    return render(request, 'index.html')

#formularz kontaktowy
def kontakt(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Formularz został poprawnie wysłany'})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = ContactForm()
    
    return render(request, 'kontakt.html', {'form': form})

#o nas

def onas(request):
    return render(request, 'o-nas.html')



# def send_email_notification(data):
#     send_mail(
#         'Nowa wiadomość kontaktowa',
#         f'Imię i nazwisko: {data["name"]}\n'
#         f'Nr telefonu: {data["phone"]}\n'
#         f'Adres e-mail: {data["email"]}\n'
#         f'Temat: {data["property-type"]}\n'
#         f'Uwagi: {data["comments"]}',
#         'adres@twojegoemaila.com',
#         ['adres@twojegoemaila.com'],
#         fail_silently=False,
#     )


#wyszukiwanie
def Search(request):
    query = request.GET.get('q')
    results = Estate.objects.filter(field__icontains=query)
    return render(request, 'search_results.html', {'results': results})

#API
def listing_view(request):
    # Pobierz dane z API
    base_url = "https://api.asariweb.pl/apiSite/listing"
    listing_id = 10985335
    headers = {
        "Content-Type": "application/json",
        "SiteAuth": "64066:1Rshgk13Wc49r2V2f88X8UN9V17hH3yj4d4J5TN1",
    }
    data = {
        "id": listing_id,
    }
    response = requests.post(base_url, headers=headers, json=data)
    if response.status_code == 200:
        listing_data = response.json()
    else:
        listing_data = None

    # Przekazanie danych do szablonu
    context = {
        'listing_data': listing_data,
    }
    return render(request, 'index.html', context)