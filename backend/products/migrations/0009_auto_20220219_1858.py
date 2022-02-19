# Generated by Django 3.2 on 2022-02-19 18:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0008_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='event_order',
        ),
        migrations.RemoveField(
            model_name='order',
            name='quantity_event',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]