FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src

RUN cd /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8082"]