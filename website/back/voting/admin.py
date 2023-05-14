from django.contrib import admin

# Register your models here.

from .models import *

[
admin.site.register(Voters),
admin.site.register(New_voters),
admin.site.register(Candidates),
admin.site.register(Vote),
admin.site.register(Wallet),
admin.site.register(Weight_arrays)
]
