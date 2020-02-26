web: gunicorn eaggregator.wsgi
worker: celery -A eaggregator worker --beat --scheduler django --loglevel=info
