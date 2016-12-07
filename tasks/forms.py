from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label="Title",
                           widget=forms.TextInput(attrs={'class': 'form-text', 'blank': 'true'}), required=False)
    description = forms.CharField(label="Description",
                           widget=forms.TextInput(attrs={'class': 'form-text', 'blank': 'true'}), required=False)
    deadline = forms.DateTimeField(label="Deadline", widget=forms.DateInput(attrs={'class': 'form-text date', 'id': 'deadline', 'type': ""}),
                                required=False)
    status = forms.CharField(label="Status (0/1)",
                           widget=forms.TextInput(attrs={'class': 'form-text', 'blank': 'true'}), required=False)
    priority = forms.CharField(label="Priority (1/2/3)",
                           widget=forms.TextInput(attrs={'class': 'form-text', 'blank': 'true'}), required=False)
