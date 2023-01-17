import os
import libtorrent as lt
import time
import datetime
from django_base_conf.settings import MEDIA_ROOT
from celery import shared_task


@shared_task()
def download_torrent(magnet_link, user_id):
    time.sleep(20)
    print("Now beginning.")
    ses = lt.session()
    ses.listen_on(6881, 6891)

    params = {
        "save_path": os.path.join(MEDIA_ROOT, "userID_" + str(user_id)),
        "storage_mode": lt.storage_mode_t(2),
        # "paused": False,
        # "auto_managed": True,
        # "duplicate_is_error": True,
    }

    link = magnet_link
    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()
    begin = time.time()
    print(datetime.datetime.now())

    print("Downloading Metadata...")
    while not handle.has_metadata():
        time.sleep(1)
    print("Got Metadata, Starting Torrent Download")

    print("starting", handle.name())

    while handle.status().state != lt.torrent_status.seeding:
        s = handle.status()
        state_str = [
            "queued",
            "checking",
            "downloading metadata",
            "downloading",
            "finished",
            "allocating",
        ]
        print(
            "%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s "
            % (
                s.progress * 100,
                s.download_rate / 1000,
                s.upload_rate / 1000,
                s.num_peers,
                state_str[s.state],
            )
        )
        time.sleep(5)
    end = time.time()
    print(handle.name(), "COMPLETE")

    print(
        "Elapsed Time: ",
        int((end - begin) // 60),
        "min:",
        int((end - begin) % 60),
        "sec:",
    )

    print(datetime.datetime.now())
