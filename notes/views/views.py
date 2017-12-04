from django.shortcuts import render
from notes.models import Category, Note


def categories_view(request):
    categories = Category.objects.all()
    return render(request, 'notes/index.html', {'categories': categories})


def notes_view(request, cid):
    notes = Note.objects.filter(category=cid)
    return render(request, 'notes/notes.html', {'notes': notes})


def note_view(request, nid):
    note = Note.objects.get(id=nid)
    return render(request, 'notes/note.html', {'note': note})
