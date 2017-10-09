from django.contrib import admin

# Register your models here.

from apps.app_gestor_usuarios.models import db_usuarios, db_manage_contacts


admin.site.register(db_usuarios)
admin.site.register(db_manage_contacts)