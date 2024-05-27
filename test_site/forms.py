from django import forms

from test_site.models import NotesModel


class NotesForm(forms.Form):
    text: forms.CharField = forms.CharField(label="Заметка")

    def save(self) -> None:
        if self.is_valid():
            NotesModel(text=self.cleaned_data.get("text")).save()
