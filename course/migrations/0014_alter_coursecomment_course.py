# Generated by Django 4.2.7 on 2023-12-11 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("course", "0013_alter_coursecomment_course"),
    ]

    operations = [
        migrations.AlterField(
            model_name="coursecomment",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, related_name="comments", to="course.course"
            ),
        ),
    ]
