from django.core.mail import send_mail
from .forms import ContactForm
from django.shortcuts import render
from .models import About



def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Send email
            send_mail(
                subject,
                f'You have a new message from {name} ({email}):\n\n{message}',
                'your_email@example.com',
                ['recipient@example.com'],
                fail_silently=False,
            )

            # Optionally, you can redirect or show a success message here
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def about(request):
    about_info = About.objects.first()  # Assuming you only have one about section, adjust as needed
    return render(request, 'about.html', {'about_info': about_info})