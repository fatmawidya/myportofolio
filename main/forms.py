from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateInput, NumberInput
from main.models import Experience, Education
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

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

    def clean_title(self):
        title = strip_tags(self.cleaned_data.get('title', '')).strip()
        if not title:
            raise ValidationError(
                'Position & Organization cannot contain only HTML tags.'
            )
        return title

    def clean_description(self):
        return strip_tags(self.cleaned_data.get('description', '')).strip()

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