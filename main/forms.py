from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput, NumberInput
from main.models import Experience, Education

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

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = ['institution', 'degree', 'field_of_study', 'start_year', 'end_year', 'thumbnail', 'description']
        labels = {
            'institution': 'Institution / School Name',
            'degree': 'Degree / Level',
            'field_of_study': 'Field of Study / Major',
            'start_year': 'Start Year',
            'end_year': 'End Year (Leave blank if currently studying)',
            'thumbnail': 'Logo URL',
            'description': 'Description',
        }
        widgets = {
            'institution': TextInput(attrs={'placeholder': 'Universitas Indonesia'}),
            'degree': Select(),
            'field_of_study': TextInput(attrs={'placeholder': 'Information Systems'}),
            'start_year': NumberInput(attrs={'placeholder': '2023'}),
            'end_year': NumberInput(attrs={'placeholder': '2027'}),
            'thumbnail': URLInput(attrs={'placeholder': 'https://example.com/logo.png (Optional)'}),
            'description': Textarea(attrs={
                'rows': 5, 
                'placeholder': 'What did you study? Any notable achievements or organizations?'
            }),
        }