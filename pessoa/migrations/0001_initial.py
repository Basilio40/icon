# Generated by Django 2.1.7 on 2019-04-17 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competencia', models.CharField(max_length=64)),
                ('categoria', models.CharField(choices=[('Plena', 'Plena'), ('Parcial', 'Parcial'), ('Deficiente', 'Deficiente')], default='Sou igual', max_length=12)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Competencia',
                'verbose_name_plural': 'Competencias',
            },
        ),
        migrations.AlterUniqueTogether(
            name='competencia',
            unique_together={('user', 'competencia')},
        ),
    ]
