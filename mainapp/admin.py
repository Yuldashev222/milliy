from django.contrib import admin
from .models import *

admin.site.register(InfoNoun)
admin.site.register(InfoAdjective)
admin.site.register(Synonym)
admin.site.register(Antonym)
admin.site.register(Hyponym)
admin.site.register(Hyperonym)