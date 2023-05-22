# Generated by Django 4.1.7 on 2023-03-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('ficher_CV', models.ImageField(upload_to='cv/')),
                ('ficher_photo', models.ImageField(upload_to='photos/')),
                ('lien_linkidin', models.URLField()),
            ],
        ),
    ]