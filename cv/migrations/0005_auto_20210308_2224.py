# Generated by Django 3.1.4 on 2021-03-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0004_auto_20210308_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicpublicinfo',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicpublicinfo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='basicpublicinfo',
            name='location',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='basicpublicinfo',
            name='phone_number',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='languageskills',
            name='level',
            field=models.IntegerField(choices=[(1, 'FUNDAMENTAL_AWARNESS'), (4, 'ADVANCED'), (3, 'INTERMEDIATE'), (2, 'NOVICE'), (5, 'EXPERT')]),
        ),
        migrations.AlterField(
            model_name='professionalskills',
            name='level',
            field=models.IntegerField(choices=[(1, 'FUNDAMENTAL_AWARNESS'), (4, 'ADVANCED'), (3, 'INTERMEDIATE'), (2, 'NOVICE'), (5, 'EXPERT')]),
        ),
    ]
