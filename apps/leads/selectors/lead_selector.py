# apps/leads/selectors/lead_selector.py

from apps.leads.models import Lead

def get_all_leads():
    return Lead.objects.all().order_by("-created_at")