
import libtorrent as lt
import time
from django_base_conf.settings import MEDIA_ROOT

def download_torrent(magnet_link, user_id):
    ses = lt.session()
    ses.listen_on(6881, 6891)

    params = {
        'save_path': os.path.join(MEDIA_ROOT, 'userID_' + str(user_id)),
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True
    }

    link = magnet_link
    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()
    begin= time.time()
    print(datetime.datetime.now())

    