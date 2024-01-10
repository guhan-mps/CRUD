FROM python:3.10
WORKDIR /code
COPY ./backendapi/config/requirements.txt /code/backendapi/config/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/backendapi/config/requirements.txt
COPY ./backendapi /code/backendapi
CMD ["uvicorn","backendapi.sql_app.main:app","--host","0.0.0.0","--port","8000","--reload"]
