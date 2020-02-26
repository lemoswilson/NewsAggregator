web: gunicorn eaggregator.wsgi
worker: celery -A eaggregator worker --loglevel=info
beat: celery -A eaggregator beat -l 
