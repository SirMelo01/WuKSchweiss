# Generated by Django 4.0.10 on 2023-10-02 15:19

from django.db import migrations, models
import yoolink.ycms.models


class Migration(migrations.Migration):

    dependencies = [
        ('ycms', '0013_blog_description_alter_textcontent_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileentry',
            name='file',
            field=models.ImageField(upload_to=yoolink.ycms.models.unique_image_name),
        ),
    ]
