web: gunicorn eaggregator.wsgi
worker: celery -A eaggregator worker --beat --loglevel=info
