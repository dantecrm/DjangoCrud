from django.shortcuts import render,render_to_response, get_object_or_404
from crud.models import Producto
from django.template import RequestContext
from crud.forms import ProductoForm
from django.http import HttpResponseRedirect, HttpResponse

def inicio(request):
    productos = Producto.objects.all().order_by('-id')
    return render(request, "crud/inicio.html", {'productos':productos})

def agregar(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/home")
    else:
        formulario = ProductoForm()
    return render_to_response("crud/agregar.html",
                              {"formulario":formulario},
                              context_instance=RequestContext(request))

def borrar(request, id):
    producto = get_object_or_404(Producto, pk = id)
    producto.delete()
    return HttpResponseRedirect("/home")

def editar(request, id):
    producto = get_object_or_404(Producto, pk=id)
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/home")
    else:
        formulario = ProductoForm(instance=producto)
    return render_to_response("crud/agregar.html",
                              {'formulario':formulario},
                              context_instance=RequestContext(request))
