from django.contrib import admin
from .models import protein_sequence,ProteinProperties
# Register your models here.
admin.site.register(protein_sequence)
admin.site.register(ProteinProperties)
