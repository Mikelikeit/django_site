from django.contrib import admin
from .models import StatusCrm, Order, OrderComment

admin.site.register(StatusCrm)
admin.site.register(Order)
admin.site.register(OrderComment)
