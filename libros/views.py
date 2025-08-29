from django.shortcuts import render, redirect, get_object_or_404
from .models import Libro
from django.contrib import messages

# Listado de libros
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, "libros/libro_list.html", {"libros": libros})

# Registrar libro
def libro_create(request):
    if request.method == 'POST':
        titulo = request.POST['txtTitulo']
        autor = request.POST['txtAutor']
        fecha = request.POST.get('fechaPublicacion')
        precio = request.POST.get('numPrecio') or 0

        Libro.objects.create(
            titulo=titulo,
            autor=autor,
            fechapublicacion=fecha if fecha else None,
            precio=precio
        )
        messages.success(request, "¡Libro registrado!")
        return redirect('libro-list')

    # GET → solo renderiza el formulario
    return render(request, "libros/libro_create.html")

# Editar libro (formulario)
def edicionLibro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    return render(request, "libros/edicionLibro.html", {"libro": libro})

# Guardar cambios de libro
def editarLibro(request):
    if request.method == 'POST':
        libro_id = request.POST['libroId']
        libro = get_object_or_404(Libro, id=libro_id)

        libro.titulo = request.POST['txtTitulo']
        libro.autor = request.POST['txtAutor']
        libro.fechapublicacion = request.POST.get('fechaPublicacion') or None
        libro.precio = request.POST.get('numPrecio') or 0
        libro.save()

        messages.success(request, "¡Libro actualizado!")
        return redirect('libro-list')

# Eliminar libro
def eliminarLibro(request, libro_id):
    libro = get_object_or_404(Libro, id=libro_id)
    libro.delete()
    messages.success(request, "¡Libro eliminado!")
    return redirect('libro-list')
