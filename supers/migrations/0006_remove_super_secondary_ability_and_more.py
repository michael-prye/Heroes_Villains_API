# Generated by Django 4.0.3 on 2022-04-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supers', '0005_remove_super_primary_ability_super_primary_ability'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='super',
            name='secondary_ability',
        ),
        migrations.AddField(
            model_name='super',
            name='secondary_ability',
            field=models.ManyToManyField(related_name='Secondary_ability', to='supers.power'),
        ),
    ]
