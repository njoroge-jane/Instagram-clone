from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import UploadImageForm

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
  return render(request,'index.html')


def upload(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            upload = form.save(commit=False)
            upload.user = current_user
            upload.save()
        return redirect('index')

    else:
        form = UploadImageForm()
    return render(request, 'new_upload.html', {"form": form})
  
def profile(request):
    return render(request, 'profile.html')