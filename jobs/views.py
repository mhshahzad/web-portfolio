from django.shortcuts import render, get_object_or_404
from .models import Job
from .forms import ContactForm
from django.core.mail import send_mail


# Create your views here.
def detail(request, job_id):
    job_detail = get_object_or_404(Job, pk=job_id)
    return render(request, 'jobs/detail.html', {'job': job_detail})


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_mail(
                'Contact Form Message',
                form.cleaned_data['message'],
                form.cleaned_data['email'],
                ['your-email@example.com'],
            )
            return render(request, 'jobs/home.html', {'form': form, 'message': 'Message sent successfully'})
    else:
        form = ContactForm()
    return render(request, 'jobs/home.html', {'form': form, "jobs": Job.objects.all()})
