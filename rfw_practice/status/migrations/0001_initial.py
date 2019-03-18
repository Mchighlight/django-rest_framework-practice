# Generated by Django 2.1.7 on 2019-03-18 07:57

from django.conf import settings
from django.db import migrations, models
import status.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to=status.models.upload_status_image)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Status post',
                'verbose_name_plural': 'Statuss post',
            },
        ),
    ]