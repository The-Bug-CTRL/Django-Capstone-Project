# candidate/migrations/0002_auto.py
from django.db import migrations

def create_initial_polls(apps, schema_editor):
    Poll = apps.get_model('candidate', 'Poll')
    Poll.objects.create(question='Page 1 Poll', option1='Option A', option2='Option B')
    Poll.objects.create(question='Page 2 Poll', option1='Option X', option2='Option Y')
    Poll.objects.create(question='Page 3 Poll', option1='Option M', option2='Option N')

class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_polls),
    ]