from django.shortcuts import render

def image_upload(request):
    return render(request, 'image_upload.html')
