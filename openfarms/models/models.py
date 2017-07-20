# -*- coding: utf-8 -*-

from django.db import models

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailcore.fields import RichTextField
from django.utils.translation import ugettext_lazy as _
from wagtail.api import APIField

from wagtail.wagtailimages.api.fields import ImageRenditionField
from .serializers import ProduceRenditionField, LabelRenditionField, RegionRenditionField

class Datasource(models.Model):
    title = models.CharField(max_length=255)
    homepage = models.URLField()
    feed = models.URLField(blank=True)
    notes = models.TextField(blank=True)
    api_fields = [
        'title', 'homepage',
    ]
    def __str__(self):
        return self.title

class Label(models.Model):
    title = models.CharField(max_length=255)
    about = models.TextField(blank=True)
    imageurl = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Region(models.Model):
    title = models.CharField(max_length=255)
    imageurl = models.URLField(blank=True)
    def __str__(self):
        return self.title

class Produce(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    panels = [
        FieldPanel('name'),
        FieldPanel('info'),
        ImageChooserPanel('image'),
    ]
    api_fields = [
        APIField('name'),
        APIField('info'),
        APIField('farms'),
        APIField('image_thumb', serializer=ImageRenditionField('width-160', source='image')),
        APIField('image_full',  serializer=ImageRenditionField('width-800', source='image')),
    ]
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Produce'

class Farm(models.Model):
    title = models.CharField(max_length=255, unique=True)
    about = RichTextField(blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    person = models.CharField(max_length=255, blank=True,
        verbose_name=_('Name of responsible contact'))
    phone = models.CharField(max_length=255, blank=True)
    mobile = models.CharField(max_length=255, blank=True)
    email = models.CharField(max_length=255, blank=True)
    website = models.URLField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    longitude = models.CharField(max_length=50, blank=True)
    latitude = models.CharField(max_length=50, blank=True)

    updated = models.DateTimeField(auto_now=True, editable=False)
    published = models.DateTimeField(auto_now_add=True, editable=False)

    is_producer = models.BooleanField(default=True,
        verbose_name='Producer',
        help_text=_('Is this a producer (and not only distributor)?'))
    produce = models.ManyToManyField(Produce, blank=True, related_name='farms')
    distributors = models.ManyToManyField("self", blank=True)

    labels = models.ManyToManyField(Label, blank=True)
    region = models.ForeignKey(Region,
        null=True, blank=True, on_delete=models.PROTECT)
    datasource = models.ForeignKey(Datasource,
        null=True, blank=True, on_delete=models.PROTECT)

    panels = [
        FieldPanel('title'),
        FieldPanel('about'),
        ImageChooserPanel('image'),
        MultiFieldPanel([
            FieldPanel('person'),
            FieldPanel('phone'),
            FieldPanel('mobile'),
            FieldPanel('email'),
            FieldPanel('website'),
            FieldPanel('address'),
            FieldPanel('longitude'),
            FieldPanel('latitude'),
        ],
        heading="Contact",
        classname="collapsible collapsed",
        ),
        MultiFieldPanel([
            FieldPanel('produce'),
            FieldPanel('labels'),
        ],
        heading="Details",
        classname="col5",
        ),
        MultiFieldPanel([
            FieldPanel('is_producer'),
            FieldPanel('distributors'),
            FieldPanel('region'),
            FieldPanel('datasource'),
        ],
        heading="Connections",
        classname="col7",
        ),
    ]

    api_fields = [
        APIField('title'), APIField('about'),
        APIField('image_thumb', serializer=ImageRenditionField('width-160', source='image')),
        APIField('image_full',  serializer=ImageRenditionField('width-800', source='image')),
        APIField('produce', serializer=ProduceRenditionField()),
        APIField('labels',  serializer=LabelRenditionField()),
        APIField('region',  serializer=RegionRenditionField()),
        APIField('distributors')
    ]
    api_meta_fields = [
        'person', 'phone', 'mobile',
        'email', 'website', 'address',
        'longitude', 'latitude',
        'is_producer',
    ]

    def __str__(self):
        return self.title