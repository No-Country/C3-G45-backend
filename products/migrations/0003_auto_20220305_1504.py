# Generated by Django 3.2 on 2022-03-05 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_id_event_ticket_ticket_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='quantity_tickets',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ticket', to='products.ticket'),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]