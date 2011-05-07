from django import forms
from models import Snippet
from formatter import formatcode

class SnippetForm(forms.ModelForm):
    def save(self, *args, **kwargs):
        kwargs['commit'] = False
        obj = super(SnippetForm, self).save(*args, **kwargs)
        obj.formatted = formatcode(obj.orign, obj.get_language_display())
        obj.save()
        return obj
    class Meta:
        model = Snippet
