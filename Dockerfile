From continuumio/miniconda3

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python -m pip install -r requirements.txt

COPY . /app/

RUN  python init_db.py 

EXPOSE 8082 

# Make Gunicorn the entrypoint program, and then feed it appropriate arguments.
ENTRYPOINT [ "gunicorn" ]
CMD [ "-b", ":8082", "wsgi:application" ]