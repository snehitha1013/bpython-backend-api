FROM python:3.11-slim

WORKDIR /code

# small deps to build some wheels if needed
RUN apt-get update && apt-get install -y build-essential gcc

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# copy app code
COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
