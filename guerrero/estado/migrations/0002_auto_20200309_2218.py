# Generated by Django 3.0.4 on 2020-03-10 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estado', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demonio',
            name='detallecuerpo',
        ),
        migrations.AddField(
            model_name='demonio',
            name='estado',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='estado.Estado'),
            preserve_default=False,
        ),
    ]
