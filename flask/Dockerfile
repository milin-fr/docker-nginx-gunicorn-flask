FROM python:3

WORKDIR /work_dir

ADD . /work_dir

RUN pip install -r requirements.txt

ENTRYPOINT ["sh", "start_app_with_gunicorn.sh"]