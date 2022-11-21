from django.contrib import admin
from api.models import CompanyModel,EmployeeModel


class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','location','domain')
	search_fields = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
	list_display = ('name','email','phone')
	list_filter = ('company',)

admin.site.register(CompanyModel,CompanyAdmin)
admin.site.register(EmployeeModel,EmployeeAdmin)
