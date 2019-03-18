from django.shortcuts import render

from .queries import *


def index(request):
    # offers = getOffers()
    offers = Offer.objects.all()
    return render(request, 'autos/index.html', locals())


def offers(request):
    offers = Offer.objects.filter(autoservice=1)
    if 'save' in request.POST:
        update_offer(request.POST['id'], 1, request.POST['service'], request.POST['text'], request.POST['cost'])

    if 'create' in request.POST:
        create_offer(request.POST['autoservice'], request.POST['service'], request.POST['text'], request.POST['cost'])

    if 'delete' in request.POST:
        delete_offer(request.POST['delete'])
    return render(request, 'autos/offers.html', locals())


def edit(request):
    if 'edit' in request.POST:
        order = get_details(request.POST['edit'])[0]
        autoservice = order.autoservice_id
    else:
        autoservice = 1
    services = get_services()
    return render(request, 'autos/edit.html', locals())


# def oneitem(request):
#     return render(request, 'autos/oneitem.html')


def oneitem(request):
    order = get_details(request.POST['view'])[0]
    return render(request, 'autos/oneitem.html', locals())
