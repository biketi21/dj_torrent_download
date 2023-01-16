from django.shortcuts import render
from files.functions import download_torrent

# Create your views here.
def home(request):
    if request.method == "POST":
        magnet_link = request.POST["magnet_link"]

        user_id = request.user.id
        print(user_id, magnet_link)
        download_torrent(magnet_link, user_id)

    return render(request, "index.html")
