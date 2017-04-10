# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-10 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_contact_contactform_contactformfield'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='on_homepage',
            field=models.BooleanField(default=False, verbose_name='Auf der Frontpage anzeigen'),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='intro_de',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='intro_fr',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='thanks_de',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='thanks_fr',
            field=wagtail.wagtailcore.fields.RichTextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='contactform',
            name='title_fr',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='infos_de',
            field=wagtail.wagtailcore.fields.StreamField((('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())))),), blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='infos_fr',
            field=wagtail.wagtailcore.fields.StreamField((('info', wagtail.wagtailcore.blocks.StructBlock((('title', wagtail.wagtailcore.blocks.CharBlock(required=True)), ('photo', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('summary', wagtail.wagtailcore.blocks.RichTextBlock(required=True)), ('action', wagtail.wagtailcore.blocks.CharBlock()), ('url', wagtail.wagtailcore.blocks.URLBlock())))),), blank=True, null=True),
        ),
    ]
