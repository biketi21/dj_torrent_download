import multiprocessing

wsgi_app = 'django_base_conf.wsgi:application'
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
# accesslog = '
# errorlog = 'home/biketi21/logs/gunicorn/error.log'
capture_output = True
loglevel = 'debug'
daemon = True

