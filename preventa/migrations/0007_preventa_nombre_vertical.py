# Generated by Django 5.0 on 2024-04-18 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preventa', '0006_alter_preventa_usuario_teknica'),
    ]

    operations = [
        migrations.AddField(
            model_name='preventa',
            name='nombre_vertical',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
