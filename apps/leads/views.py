from django.shortcuts import redirect, HttpResponse
from apps.leads.services.lead_service import create_lead
from .tasks import send_lead_email

def submit_lead(request):
    if request.method == "POST":

        create_lead(request.POST)

        send_lead_email.delay(
            request.POST.get("name"),
            request.POST.get("email"),
            request.POST.get("phone"),
            request.POST.get("message"),
        )
    

        return redirect("/?success=1")

    return redirect("/")

