FROM python:3.12-slim
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask
RUN useradd -m appuser
USER appuser
EXPOSE 5000
CMD ["python", "app.py"]
