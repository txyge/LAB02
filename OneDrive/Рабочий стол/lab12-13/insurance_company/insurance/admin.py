from django.contrib import admin
from .models import Client, Policy, Claim

class ClaimInline(admin.TabularInline):
    model = Claim
    extra = 1

class PolicyAdmin(admin.ModelAdmin):
    list_display = ('policy_number', 'client', 'coverage_amount', 'start_date', 'end_date')
    list_filter = ('client',)
    inlines = [ClaimInline]

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

admin.site.register(Client, ClientAdmin)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Claim)