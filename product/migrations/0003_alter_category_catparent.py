# Generated by Django 4.0.6 on 2022-07-15 01:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_productimage_prdimimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, limit_choices_to={'CATParent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.category', verbose_name='sub category'),
        ),
    ]
