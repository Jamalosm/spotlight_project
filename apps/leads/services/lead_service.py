from apps.leads.models import Lead

def create_lead(data):
    return Lead.objects.create(
        name=data.get("name"),
        email=data.get("email"),
        phone=data.get("phone"),
        message=data.get("message")
    )