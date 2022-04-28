# Generated by Django 4.0.4 on 2022-04-28 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PDF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namePDF', models.CharField(max_length=50, verbose_name='')),
                ('base64', models.CharField(max_length=50, verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.CharField(max_length=20, verbose_name='')),
                ('labNumber', models.PositiveSmallIntegerField(default=1, verbose_name='')),
                ('name', models.CharField(max_length=100, verbose_name='')),
                ('points', models.PositiveSmallIntegerField(default=0, verbose_name='')),
                ('githubURL', models.SlugField(max_length=150, unique=True)),
                ('reportID', models.CharField(max_length=150, verbose_name='')),
                ('pdf', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='API.pdf')),
            ],
        ),
    ]