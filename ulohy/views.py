from django.shortcuts import render, redirect
from .models import Uloha
from .forms import UlohaForm

def zoznam_uloh(request):
    ulohy = Uloha.objects.all()
    return render(request, 'ulohy/zoznam.html', {'ulohy':ulohy})

def oznac_hotovu(request, id):
    uloha = Uloha.objects.get(id=id)
    if uloha.hotova:
        uloha.delete()
    else:
        uloha.hotova = not uloha.hotova
        uloha.save()
    return redirect('zoznam_uloh')

def pridat_ulohu(request):
    if request.method == 'POST':
        form = UlohaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('zoznam_uloh')    
    else:
        form = UlohaForm()
    return render(request, 'ulohy/formular.html', {'form':form})