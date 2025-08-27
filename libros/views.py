from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm  # vamos a crear este form

# Lista de libros
def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'libros/libro_list.html', {'libros': libros})

# Detalle de un libro
def libro_detail(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, 'libros/libro_detail.html', {'object': libro})

# Crear libro
def libro_create(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libro-list')
    else:
        form = LibroForm()
    return render(request, 'libros/libro_form.html', {'form': form})

# Editar libro
def libro_update(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libro-list')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/libro_form.html', {'form': form})

# Eliminar libro
def libro_delete(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    if request.method == 'POST':
        libro.delete()
        return redirect('libro-list')
    return render(request, 'libros/libro_confirm_delete.html', {'object': libro})

