# Generated by Django 4.0.5 on 2022-06-06 19:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('dimension', models.IntegerField()),
                ('date', models.DateTimeField()),
                ('type', models.CharField(choices=[('Document', 'Document'), ('Image', 'Image'), ('Audio', 'Audio'), ('Video', 'Video'), ('Unknown', 'Unknown')], default='Unknown', max_length=8)),
                ('myId', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('mail', models.CharField(max_length=128)),
                ('myId', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Autorization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autorization', models.CharField(max_length=128)),
                ('myId', models.CharField(max_length=128)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.file')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]