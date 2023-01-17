import os
from django.shortcuts import render
from files.tasks import download_torrent
from django_base_conf.settings import MEDIA_ROOT

# Create your views here.
def home(request):
    if request.method == "POST":
        magnet_link = request.POST["magnet_link"]

        user_id = request.user.id
        print(user_id, magnet_link)
        download_torrent.delay(magnet_link, user_id)

    return render(request, "index.html")


def files(request):
    if request.method == "GET":
        user_id = request.user.id

        path = os.path.join(MEDIA_ROOT, "UserID_" + str(user_id))
        file_lst = []
        final_lst = []

        for root, dirs, files in os.walk(path):
            for file in files:
                file_lst.append(os.path.join(root, file))

        for name in file_lst:
            name.strip("/home/biketi21/Django9/torr/torr/media/")
            final_lst.append(name)

    return final_lst
