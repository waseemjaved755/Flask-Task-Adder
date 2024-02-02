
FROM python:3.8-slim


WORKDIR /app

# Create and activate virtual environment
RUN python3 -m venv venv
ENV PATH="/app/venv/bin:$PATH"

COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000

CMD ["python3", "main.py"]
