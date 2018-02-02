from django.contrib import admin
from .models import Patient,MedicalHistory,Hereditary

admin.site.register(Patient)
admin.site.register(MedicalHistory)
admin.site.register(Hereditary)
