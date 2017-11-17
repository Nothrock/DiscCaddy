from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from pages.models import User, Course, CheckIn, Hole, CheckInImage, Friend
from django import forms
from pages.forms import UserForm
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.db.models import Q


@login_required
def map_search(request):
    course = Course.objects.all()
    return render(request, 'pages/map_search.html', {'courses': course})


@login_required
def courses(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request, 'pages/courses.html', {'course': course})


def find_username(request):
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST.get('username', None)).exists()
        return JsonResponse({'user': not user})
    return JsonResponse({'error': 'You shouldn\'t be here'})


@login_required
def profile(request, username):
    unique = request.user.my_check_in.values('hole_number__course__name').distinct().count()
    return render(request, 'pages/profile.html', {'unique': unique})


@login_required
def my_bag(request):
    return render(request, 'pages/my_bag.html')


@login_required
def news(request):
    return render(request, 'pages/news.html')


@login_required
def settings(request):
    return render(request, 'pages/settings.html')


@login_required
def friends(request):
    # all_friends = Friend.objects.filter((Q(requestor__username=request.user.username) | Q(requestee__username=request.user.username)) & Q(accepted=True))
    all_friends = Friend.objects.friends(request.user.username)
    return render(request, 'pages/friends.html', {'all_friends': all_friends})


@login_required
def add_friends(request):
    friend_request = Friend.objects.filter(Q(requestee__username=request.user.username) & Q(accepted=None))
    return render(request, 'pages/add_friends.html', {'friend_request': friend_request})

@login_required
def accept_friend(request):
    if request.method == 'POST':
        f = Friend.objects.get(pk=request.POST.get('id'))
        f.accepted = True
        f.save()
        return JsonResponse({'message': 'Success'})
    return JsonResponse({'error': 'You shouldn\'t be here'})


@login_required
def reject_friend(request):
    if request.method == 'POST':
        f = Friend.objects.get(pk=request.POST.get('id'))
        f.accepted = False
        f.save()
        return JsonResponse({'message': 'Success'})
    return JsonResponse({'error': 'You shouldn\'t be here'})


@login_required
def activity(request):
    user_check_ins = request.user.my_check_in.all()
    return render(request, 'pages/activity.html', {'user_check_ins': user_check_ins})


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST, files=request.FILES)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'pages/register.html', {'user_form': user_form, 'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('map_search'))
            else:
                return HttpResponse("Your Disc Caddy account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'pages/login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('map_search'))


@login_required
def check_in_form(request):
    if request.method == 'POST':
        art = CheckIn()
        art.user = request.user
        # TODO: programmatically get hole ID
        art.hole_number = Hole.objects.get(pk=request.POST.get('hole_number', None))
        art.user_comment = request.POST.get('UserComment', None)
        art.hole_rating = request.POST.get('rating', None)
        art.user_score = request.POST.get('my_score', None)
        art.save()
        img = request.FILES.get('photo')
        if img:
            i = CheckInImage()
            i.img = img
            i.check_in = art
            i.save()
        # TODO: change to JSON response
        return HttpResponseRedirect('/')
    return render(request,  'pages/check_in_form.html')
