# Generated by Django 3.2.3 on 2021-07-18 22:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoExampleApplication', '0002_auto_20210313_1049'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericAttachment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('file', models.FileField(upload_to='', verbose_name='Object Upload (to default storage)')),
            ],
        ),
    ]