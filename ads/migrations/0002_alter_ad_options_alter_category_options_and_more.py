# Generated by Django 4.1.2 on 2022-10-26 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_alter_user_options_alter_location_lat_and_more"),
        ("ads", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="ad",
            options={
                "ordering": ["-price"],
                "verbose_name": "Объявление",
                "verbose_name_plural": "Объявления",
            },
        ),
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ["name"],
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.AlterField(
            model_name="ad",
            name="author",
            field=models.ForeignKey(
                default="", on_delete=django.db.models.deletion.CASCADE, to="users.user"
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="category",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="ads.category",
            ),
        ),
        migrations.AlterField(
            model_name="ad",
            name="description",
            field=models.TextField(default="", max_length=300),
        ),
        migrations.AlterField(
            model_name="ad",
            name="image",
            field=models.ImageField(null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="ad",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="ad",
            name="name",
            field=models.CharField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="ad",
            name="price",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(default="", max_length=50),
        ),
    ]