FROM python:latest

RUN mkdir /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache -r requirements.txt
RUN pip install .devopstraininglab02-1.0.0-py2.py3-none-any.whl

EXPOSE 8088

CMD ["python","app.py"]