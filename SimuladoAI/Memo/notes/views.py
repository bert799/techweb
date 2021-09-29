from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note(title = title, details = content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        last_note = all_notes.last()
        return render(request, 'notes/index.html', {'note': last_note})

def delete(request):
    id = request.POST.get('id')
    note = Note.objects.filter(id=id)
    note.delete()
    return redirect('index')

def update(request):
    id = request.POST.get('id')
    title = request.POST.get('title')
    details = request.POST.get('details')
    note = Note.objects.filter(id=id)
    note.update(title = title, details = details)
    return redirect('index')