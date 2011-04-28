from django.contrib import admin

from isotests.models import Iso, Architecture, IsoType, BootType
from isotests.models import HardwareType, InstallType, Source
from isotests.models import ClockChoice, Filesystem, Module, Bootloader

admin.site.register(Iso)
admin.site.register(Architecture)
admin.site.register(IsoType)
admin.site.register(BootType)
admin.site.register(HardwareType)
admin.site.register(InstallType)
admin.site.register(Source)
admin.site.register(ClockChoice)
admin.site.register(Filesystem)
admin.site.register(Module)
admin.site.register(Bootloader)

# vim: set ts=4 sw=4 et:
