from django.shortcuts import render, redirect
from .forms import MahaForm
from .models import Maha


def create_view(request):
    template_name = "area/create.html"
    form = MahaForm()
    if request.method == 'POST':
        form = MahaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    context = {"form": form}
    return render(request, template_name, context)


def show_view(request):
    orders = Maha.objects.all()
    template_name = "area/show.html"
    context = {"orders": orders}
    return render(request, template_name, context)


def update_view(request, pk):
    obj = Maha.objects.get(id=pk)
    form = MahaForm(instance=obj)
    if request.method == "POST":
        form = MahaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_url")
    template_name = "area/create.html"
    context = {"form": form}
    return render(request, template_name)


def cancel_view(request, pk):
    obj = Maha.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('show_url')
    return render(request, 'area/confirmation.html')
