from django.db import migrations

def create_superuser(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    if not User.objects.filter(username='fatmawidya').exists():
        User.objects.create_superuser('fatmawidya', 'fatma.widya@ui.ac.id', 'Ftmwdy30')

class Migration(migrations.Migration):
    dependencies = [
        ('main', '0004_education_...'),  # GANTI '0004_education_...' dengan nama lengkap file 0004 kamu (tanpa .py)
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]