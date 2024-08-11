
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .constants import ACCOUNT_TYPE, GENDER_TYPE
from django.contrib.auth.models import User
from .models import UserAccount, UserAddress

class UserRegistrationForm(UserCreationForm):
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'account_type', 'city', 'street_address']
        
        # form.save()
    def save(self, commit=True):
        our_user = super().save(commit=False) # ami database e data save korbo na ekhn
        if commit == True:
            our_user.save() # user model e data save korlam
            account_type = self.cleaned_data.get('account_type')
            city = self.cleaned_data.get('city')
            street_address = self.cleaned_data.get('street_address')
            
            UserAddress.objects.create(
                user = our_user,
                city = city,
                street_address = street_address
            )
            UserAccount.objects.create(
                user = our_user,
                account_type  = account_type,
                account_no = 100000+ our_user.id
            )
        return our_user
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                
                'class' : (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                ) 
            })


# profile ki ki jinis update korte parbe amader user

class UserUpdateForm(forms.ModelForm):
    
    account_type = forms.ChoiceField(choices=ACCOUNT_TYPE)
    street_address = forms.CharField(max_length=100)
    city = forms.CharField(max_length= 100)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.account
                user_address = self.instance.address
            except UserAccount.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['account_type'].initial = user_account.account_type
                self.fields['street_address'].initial = user_address.street_address
                self.fields['city'].initial = user_address.city
                

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user) # jodi account thake taile seta jabe user_account ar jodi account na thake taile create hobe ar seta created er moddhe jabe
            user_address, created = UserAddress.objects.get_or_create(user=user) 

            user_account.account_type = self.cleaned_data['account_type']
            user_account.save()

            user_address.street_address = self.cleaned_data['street_address']
            user_address.city = self.cleaned_data['city']
            user_address.save()

        return user