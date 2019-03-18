from django.db import connection

from .models import *


def get_all_offers():
    return Offer.objects.raw("select offer.id, service.name as service, autoservice.name as autoservice, offer.text as text, offer.cost "
                  "from service, autoservice, offer "
                  "where offer.autoservice_id=autoservice.id AND offer.service_id=service.id")


def get_offers():
    return Offer.objects.raw("select * from offer")


def get_details(id):
    return Offer.objects.raw("select * from offer where offer.id=%s" % id)


def get_services():
    return Service.objects.all()


def update_offer(id, autoservice, service, text, cost):
    with connection.cursor() as c:
        c.execute("update offer set cost=%s, text='%s', service_id=%s where id=%s" % (cost, text, service, id))


def delete_offer(id):
    with connection.cursor() as c:
        c.execute("delete from Offer where id=%s" % (id))


def create_offer(autoservice, service, text, cost):
    with connection.cursor() as c:
        c.execute("insert into Offer (autoservice_id, service_id, text, cost) values (%s, %s, '%s', %s)" % (autoservice, service, text, cost))
