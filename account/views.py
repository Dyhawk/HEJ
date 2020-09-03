from django.shortcuts import render
from .forms import UserRegistrationForm, ProfileRegistrationForm, \
                   UserEditForm, ProfileEditForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def register(request):
    user_form = UserRegistrationForm(request.POST)
    profile_form = ProfileRegistrationForm(request.POST)
    if request.method == 'POST':
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            new_profile_user = new_user.username
            if profile_form.is_valid():
                new_profile = profile_form.save(commit=False)
                new_profile.user = User.objects.get(
                    username= str(new_profile_user)
                )
                new_profile.save()
                return render(request, 'account/register_done.html',
                             {'user_form': user_form,
                             'profile_form': profile_form})

        else:
            user_form = UserRegistrationForm(request.POST)
            profile_form = ProfileRegistrationForm(request.POST)

    return render(request, 'account/register.html', {
                          'user_form': user_form,
                          'profile_form': profile_form
                                                    })

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile,
                                    data=request.POST,
                                    files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return render(request, 'account/dashboard.html',
                             {'user_form': user_form,
                             'profile_form': profile_form})
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
                                    instance=request.user.profile)
    return render(request,
                  'account/edit.html',
                  {'user_form': user_form,
                   'profile_form': profile_form})

@login_required
def dashboard(request):
    return render(request, 'account/dashboard.html',
                            {'section': 'dashboard'})