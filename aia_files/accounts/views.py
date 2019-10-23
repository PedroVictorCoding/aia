from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def profile(request,pk=None):
    user    = request.user
    users   = User.objects.exclude(id=request.user.id)
    args    = {'user': user, 'users': users}
    return render(request, 'accounts/profile.html', args)
