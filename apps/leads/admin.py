from django.contrib import admin
from .models import Lead
import csv
from django.http import HttpResponse


def export_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=leads.csv'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Email', 'Phone', 'Message', 'Status'])

    for obj in queryset:
        writer.writerow([obj.name, obj.email, obj.phone, obj.message, obj.status])

    return response


export_csv.short_description = "Export Selected Leads"


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):

    list_display = ("name", "email", "phone", "status", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("name", "email", "phone")

    list_editable = ("status",)
    ordering = ("-created_at",)

    actions = [export_csv]