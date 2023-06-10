from django.shortcuts import render


def streams(request):
    return render(request, 'vid_stream/streams.html')
