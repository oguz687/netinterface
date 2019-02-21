from django.shortcuts import render

from django.http import HttpResponse
from yapayzekacore import Yapayzeka
from django.views.generic import ListView,TemplateView
from .models import Tahmin
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    orn = Yapayzeka()
    predict = orn.predict_from_model()
    model = Tahmin(tahmin=predict[0],metin=predict[1])
    print(predict[0])
    model.save()
    context = {"tahminler":Tahmin.tahmin.join()}

    return HttpResponse(template.render(context,request))
