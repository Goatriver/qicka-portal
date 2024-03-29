# Generated by Django 3.1.4 on 2021-03-08 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0003_auto_20210308_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicpublicinfo',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fi', 'Suomi')], default='fi', max_length=2),
        ),
        migrations.AddField(
            model_name='education',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fi', 'Suomi')], default='fi', max_length=2),
        ),
        migrations.AddField(
            model_name='experience',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fi', 'Suomi')], default='fi', max_length=2),
        ),
        migrations.AddField(
            model_name='otherinterests',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fi', 'Suomi')], default='fi', max_length=2),
        ),
        migrations.AddField(
            model_name='socials',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fi', 'Suomi')], default='fi', max_length=2),
        ),
        migrations.AlterField(
            model_name='languageskills',
            name='level',
            field=models.IntegerField(choices=[(1, 'FUNDAMENTAL_AWARNESS'), (5, 'EXPERT'), (4, 'ADVANCED'), (3, 'INTERMEDIATE'), (2, 'NOVICE')]),
        ),
        migrations.AlterField(
            model_name='professionalskills',
            name='level',
            field=models.IntegerField(choices=[(1, 'FUNDAMENTAL_AWARNESS'), (5, 'EXPERT'), (4, 'ADVANCED'), (3, 'INTERMEDIATE'), (2, 'NOVICE')]),
        ),
        migrations.AlterField(
            model_name='socials',
            name='service',
            field=models.TextField(choices=[('GITHUB', 'GitHub'), ('LINKEDIN', 'LinkedIn'), ('FACE', 'Facebook'), ('INSTA', 'Instagram')]),
        ),
    ]
