# Generated by Django 4.2.7 on 2023-12-11 06:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0005_course_lessons_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="course",
            name="language",
            field=models.CharField(
                choices=[("uz", "O`zbek tili"), ("en", "Ingliz tili"), ("ru", "Rus tili")], default="uz", max_length=2
            ),
        ),
    ]
