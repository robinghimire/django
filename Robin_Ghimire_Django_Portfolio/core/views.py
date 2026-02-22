from django.views.generic import TemplateView
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import ContactMessage


class HomeView(TemplateView):
    template_name = 'core/home.html'


@require_http_methods(["POST"])
def submit_contact_message(request):
    """Handle contact form submissions and save to database"""
    try:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        subject = request.POST.get('subject', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate required fields
        if not all([name, email, subject, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields.'
            }, status=400)

        # Create and save contact message
        contact_msg = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            subject=subject,
            message=message
        )

        return JsonResponse({
            'success': True,
            'message': 'Thank you! Your message has been received. We will get back to you soon.'
        })

    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': f'An error occurred: {str(e)}'
        }, status=500)
