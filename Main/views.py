from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from.filters import ResearchFilter, ProfileFilter

from django.contrib.auth.models import User
from.models import *
from Accounts.forms import EditProfile
from .forms import AddResearch
# Create your views here.


@login_required
def home(request):
    user = request.user.profile

    relevant_researches = user.researches.all()

    interests = user.interests.all()
    if interests.exists():
        relevant_researches |= Research.objects.filter(field__in=interests)
        related_users = set(User.objects.filter(profile__interests__in=interests).exclude(profile=request.user.profile))
        filter = ResearchFilter(request.GET, queryset=relevant_researches)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfile(instance=user)
    context = {
        'researches': set(filter.qs),
        'filter': filter,
        'related_accounts': related_users,
        'form': form
    }

    return render(request, 'index.html', context)


@login_required
def create_research(request):
    user = request.user.profile
    if request.method == "POST":
        form = AddResearch(request.POST, request.FILES)
        if form.is_valid():
            myform = form.save()
            user.researches.add(myform)
            user.save()
            return redirect(f"/profile")
    else:
        form = AddResearch()
    context = {
        "form": form
    }
    return render(request, "add_research.html", context)


@login_required
def research(request, id):
    research = Research.objects.get(id=id)
    owners = User.objects.filter(profile__researches=research).distinct()

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfile(instance=request.user.profile)

    context = {
        'research': research,
        'owners': owners,
        'form': form,
    }
    return render(request, 'research.html', context)


@login_required
def report(request, id):
    return render(request, "confirm.html")


@login_required
def report_confirm(request, id):
    content = Research.objects.get(id=id)
    Report.objects.create(reporter=request.user, content=content)
    return redirect("/")


@login_required
def profile(request):
    profile = request.user.profile

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfile(instance=request.user.profile)

    context = {
        "profile": profile,
        'form': form,
    }
    return render(request, "Profile.html", context)


@login_required
def field(request, id):
    profile = request.user.profile
    field = Interest.objects.get(id=id)
    researches = Research.objects.filter(field=field)
    filter = ResearchFilter(request.GET, queryset=researches)

    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfile(instance=request.user.profile)

    context = {
        "profile": profile,
        'form': form,
        'researches': filter.qs,
        'fileter': filter,
        'field': field
    }
    return render(request, "filter.html", context)


@login_required
def search(request):
    profile = request.user.profile
    researches = Research.objects.all()
    filter = ResearchFilter(request.GET, queryset=researches)
    accounts = User.objects.all()
    a_filter = ProfileFilter(request.GET, queryset=accounts)
    if request.method == "POST":
        form = EditProfile(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = EditProfile(instance=request.user.profile)

    context = {
        "profile": profile,
        "profiles": a_filter.qs,
        'form': form,
        'researches': filter.qs,
        'filter': filter,
        'a_filter': a_filter
    }
    return render(request, "search.html", context)
