from django import forms


class RecordForm(forms.Form):
    record_id = forms.CharField(help_text="Enter TNA Record ID.")
