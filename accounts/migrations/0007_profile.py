# Generated by Django 4.2.2 on 2023-08-31 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('introduction_text', models.TextField()),
                ('birthday', models.TextField()),
                ('location', models.TextField()),
            ],
        ),
    ]