FROM python:3.12-slim
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt requirements.lock ./
RUN python -m pip install --no-cache-dir -c requirements.lock -r requirements.txt
COPY generator.py utils.py ./
USER 10001:10001
CMD ["python","generator.py","--num-records","3","--output","/tmp/data.csv"]
