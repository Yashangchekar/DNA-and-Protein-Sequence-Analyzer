from django.contrib import admin
from .models import dna_sequence,dna_info
# Register your models here.
admin.site.register(dna_sequence)
admin.site.register(dna_info)
