# Generated by Django 5.0 on 2024-04-16 20:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('preventa', '0003_rename_cliente_preventa_nombre_cliente_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='preventa',
            old_name='nombre_cliente',
            new_name='id_cliente',
        ),
    ]
