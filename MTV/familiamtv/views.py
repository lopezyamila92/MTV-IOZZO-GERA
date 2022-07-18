from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

# Create your views here.

from familiamtv.models import Familia

def familia(self, nombree, parentezco, edad):

    familia = Familia(nombre=nombree, parentezco=parentezco, edad=edad)
    familia.save()

    return HttpResponse(f"""<p>Nombre: {familia.nombre} - Parentezco: {familia.parentezco} - Edad: {familia.edad} </p>""")


def familiaplantilla(self, apado, relacion, anos):

    familiaplantilla = Familia(nombre=apado, parentezco=relacion, edad=anos)
    familiaplantilla.save()

    dic = {"apado":apado, "relacion":relacion, "anos":anos}

    plantilla2 = loader.get_template("templates.html")

    documento2 = plantilla2.render(dic)

    return HttpResponse(documento2)


def comosellaman(request):

    lista_nombres = ["Sonia","Eduardo","Olga"]

    diccionario = {"nombress":lista_nombres}

    plantilla = loader.get_template("templates2.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

