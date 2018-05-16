import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.translation import pgettext_lazy


class Station(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # Translators: Station
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    website = models.URLField(verbose_name=_('Website'), blank=True)
    active = models.BooleanField(verbose_name=pgettext_lazy('Station', 'Active'), default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-active', 'name']
        verbose_name = _('Station')
        verbose_name_plural = _('Stations')


class Show(models.Model):
    # Translators: Show
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    station = models.ForeignKey('badia.Station', models.PROTECT, related_name='shows', verbose_name=_('Station'))
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    description = models.TextField(verbose_name=_('Description'), blank=True)
    website = models.URLField(verbose_name=_('Website'), blank=True)
    active = models.BooleanField(verbose_name=pgettext_lazy('Show', 'Active'), default=True)
    start = models.DateField(verbose_name=pgettext_lazy('Show', 'Start'))
    end = models.DateField(verbose_name=pgettext_lazy('Show', 'End'), blank=True)
    links = models.ManyToManyField('badia.Link', verbose_name=_('Links'))

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-active', 'name']
        verbose_name = _('Show')
        verbose_name_plural = _('Shows')


class Emission(models.Model):
    # Translators: Emission
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    show = models.ForeignKey('badia.Show', models.PROTECT, related_name='emissions', verbose_name=_('Emissions'))
    priority = models.PositiveIntegerField(verbose_name=_('Priority'), default=0)
    is_repeat = models.BooleanField(verbose_name=_('Is Repeat'), default=False)
    is_live = models.BooleanField(verbose_name=_('Is Live'), default=True)

    # These two are inherited from the parent Show (but can be changed manually if needed, eg. for a special emission)
    start = models.DateField(verbose_name=pgettext_lazy('Emission', 'Start'))
    end = models.DateField(verbose_name=pgettext_lazy('Emission', 'End'), blank=True)

    # Only the day and hour fields are used
    start_time = models.DateTimeField(verbose_name=pgettext_lazy('Emission', 'Start Time'))
    end_time = models.DateTimeField(verbose_name=pgettext_lazy('Emission', 'End Time'), blank=True)


class Link(models.Model):
    # Translators: Link
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    target = models.URLField(verbose_name=_('Target'))
    icon = models.CharField(verbose_name=_('Icon'), max_length=100, blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.name, self.target)

    class Meta:
        verbose_name = _('Link')
        verbose_name_plural = _('Links')


class LinkTemplate(models.Model):
    # Translators: LinkTemplate
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    target_template = models.CharField(verbose_name=_('Target template'), max_length=255)
    icon = models.CharField(verbose_name=_('Icon'), max_length=100, blank=True)
    help_text = models.TextField(verbose_name=_('Help Text'))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Link Template')
        verbose_name_plural = _('Link Templates')
