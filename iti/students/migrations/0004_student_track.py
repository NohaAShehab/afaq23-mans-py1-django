# Generated by Django 4.2.4 on 2023-08-09 11:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracks', '0001_initial'),
        ('students', '0003_student_created_at_student_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tracks.track'),
        ),
    ]
