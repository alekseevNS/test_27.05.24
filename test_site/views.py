from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from test_site.forms import NotesForm
from test_site.models import NotesModel


def index_page(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        note_form = NotesForm(request.POST)
        note_form.save()
    else:
        note_form = NotesForm()

    context = {
        "note_form": note_form,
        "notes_data": NotesModel.objects.all()
    }

    return render(request, "test_site/index.html", context)
