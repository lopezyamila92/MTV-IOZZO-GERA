from datetime import datetime
from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

# Create your views here.

from familiamtv.models import Familia

def familia(self, nombree, parentezco, edad):

    familia = Familia(nombre=nombree, parentezco=parentezco, edad=edad)
   

    return HttpResponse(f"""<p>Nombre: {familia.nombre} - Parentezco: {familia.parentezco} - Edad: {familia.edad} </p>""")


def familiaplantilla(self, apado, relacion, anos, cumpleanos):

    familiaplantilla = Familia(nombre=apado, parentezco=relacion, edad=anos, fecha_nacimiento=cumpleanos)
    familiaplantilla.save()

    dic = {"apado":apado, "relacion":relacion, "anos":anos, "cumpleanos":cumpleanos}

    plantilla2 = loader.get_template("templates.html")

    documento2 = plantilla2.render(dic)

    return HttpResponse(documento2)


def comosellaman(request):

    lista_nombres = ["yami","laura","marce"]

    diccionario = {"nombress":lista_nombres}

    plantilla = loader.get_template("template2.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)


def lista_familia(self):
    lista_f = Familia.objects.all()

    dic = {"familialista":lista_f}

    plantilla = loader.get_template("lista_familia.html")

    documento = plantilla.render(dic)

    return HttpResponse(documento)

    #return render(self, "lista_familia.html", {"lista_familia":lista})


