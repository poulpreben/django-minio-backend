# Generated by Django 2.2.1 on 2019-06-02 20:24

import Attachments.models
from django.db import migrations, models
import django.db.models.deletion
import django_minio_backend.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Public Attachment ID')),
                ('object_id', models.PositiveIntegerField(verbose_name="Related Object's ID")),
                ('file', models.FileField(storage=django_minio_backend.models.MinioBackend(is_public=True), upload_to=django_minio_backend.models.iso_date_prefix, verbose_name='Object Upload')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Content Type')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateAttachment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='Public Attachment ID')),
                ('object_id', models.PositiveIntegerField(verbose_name="Related Object's ID")),
                ('file', models.FileField(storage=django_minio_backend.models.MinioBackend(is_public=False), upload_to=Attachments.models.PrivateAttachment.set_file_path_name, verbose_name='Object Upload')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='Content Type')),
            ],
        ),
    ]