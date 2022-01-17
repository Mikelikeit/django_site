from django.shortcuts import render
from .models import CmsSlider
from price.models import PriceCard, PriceTable
from crm.forms import OrderForm


def first_page(request):
    slider_lst = CmsSlider.objects.all()
    card1 = PriceCard.objects.get(pk=1)
    card2 = PriceCard.objects.get(pk=2)
    card3 = PriceCard.objects.get(pk=3)
    table_lst = PriceTable.objects.all()
    form = OrderForm()
    return render(request, './index.html', {'slider_lst': slider_lst,
                                            'card1': card1,
                                            'card2': card2,
                                            'card3': card3,
                                            'table_lst': table_lst,
                                            'form': form})
