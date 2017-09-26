from django.shortcuts import render
from .models import Profile, Certification


def profile_list(request):
    profile_list = Profile.objects.all()
    # print(profile_list[0].get_gender_display())
    return render(request, 'training_management/profile_list.html', {'profile_list':profile_list})


def profile_detail(request, pk):
    profile = Profile.objects.get(pk=pk)
    certification = Certification.objects.get(user_profile=profile)
    return render(request, 'training_management/profile_detail.html', {'profile':profile,'certification':certification})



