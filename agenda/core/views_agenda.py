from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agenda
from .forms_agenda import AgendaForm

def agenda_list(request):
    contatos = Agenda.objects.filter(owner=request.user)
    return render(request, 'agenda/agenda_list.html', {'contatos': contatos})

def agenda_create(request):
    if request.method == 'POST':
        form = AgendaForm(request.POST)
        if form.is_valid():
            contato = form.save(commit=False)
            contato.owner = request.user
            contato.save()
            return redirect('agenda_list')
    else:
        form = AgendaForm()
    return render(request, 'agenda/agenda_form.html', {'form': form})

def agenda_update(request, pk):
    contato = get_object_or_404(Agenda, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = AgendaForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('agenda_list')
    else:
        form = AgendaForm(instance=contato)
    return render(request, 'agenda/agenda_form.html', {'form': form, 'agenda': contato})

def agenda_delete(request, pk):
    contato = get_object_or_404(Agenda, pk=pk, owner=request.user)
    if request.method == 'POST':
        contato.delete()
        return redirect('agenda_list')
    return render(request, 'agenda/agenda_confirm_delete.html', {'agenda': contato})
