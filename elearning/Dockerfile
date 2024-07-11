FROM python:3.9-alpine
ADD . /code
WORKDIR /code

EXPOSE 5000
ENV PORT 5000

RUN pip install -r requirements.txt
RUN pip uninstall -y flask-sqlalchemy
RUN pip install flask-sqlalchemy

RUN export FLASK_APP=app.py && export FLASK_ENV=development
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000" ]
