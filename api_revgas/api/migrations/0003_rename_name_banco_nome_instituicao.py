# Generated by Django 5.0.4 on 2024-04-13 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_banco_delete_banks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banco',
            old_name='name',
            new_name='nome_instituicao',
        ),
    ]