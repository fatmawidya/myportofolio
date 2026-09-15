from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput
from main.models import Experience

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ['title', 'category', 'thumbnail', 'started_at', 'ended_at', 'description']
        labels = {
            'title': 'Position & Organization / Company Name',
            'category': 'Experience Category',
            'thumbnail': 'Image / Logo URL',
            'started_at': 'Start Date',
            'ended_at': 'End Date (Leave blank if present)',
            'description': 'Description',
        }
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Member of Public Relations & SMM - BEM FASILKOM UI',
            }),
            'category': Select(),
            'thumbnail': URLInput(attrs={
                'placeholder': 'https://example.com/logo.png (Optional)',
            }),
            'started_at': DateInput(attrs={
                'type': 'date',
            }),
            'ended_at': DateInput(attrs={
                'type': 'date',
            }),
            'description': Textarea(attrs={
                'rows': 5,
                'placeholder': 'Write your key responsibilities and achievements here.',
            }),
        }