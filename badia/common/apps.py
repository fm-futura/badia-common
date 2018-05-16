from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CommonConfig(AppConfig):
    name = 'badia.common'
    label = 'badia'
    verbose_name = _('Badia - Common Settings')
