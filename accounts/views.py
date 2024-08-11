from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect

# class UserRegistrationView(FormView):
#     template_name = 'accounts/user_registration.html'
#     form_class = UserRegistrationForm
#     success_url = reverse_lazy('profile')
    
#     def form_valid(self,form):
#         print(form.cleaned_data)
#         user = form.save()
#         login(self.request, user)
#         print(user)
#         return super().form_valid(form)
    

from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('info')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        
        # Send confirmation email
        self.send_confirmation_email(user)

        return super().form_valid(form)

    def send_confirmation_email(self, user):
        subject = 'Welcome to Our Site!'
        message = f'Hi {user.username},\n\nThank you for registering at our site. Your account has been created successfully.\n\nBest regards,\nYour Site Team'
        from_email = settings.DEFAULT_FROM_EMAIL
        recipient_list = [user.email]
        
        send_mail(subject, message, from_email, recipient_list)

class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('index')

def user_logout(request):
    logout(request)
    return redirect(reverse_lazy('index'))



class UserAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to the user's profile page
        return render(request, self.template_name, {'form': form})
    


from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_confirmation_email(self, user):
    subject = 'Welcome to Our Site!'
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [user.email]
    
    # Render the HTML email template
    message = render_to_string('registration_email.html', {'user': user})

    # Send the email
    email = EmailMessage(subject, message, from_email, recipient_list)
    email.content_subtype = 'html'  # Important for HTML emails
    email.send()
