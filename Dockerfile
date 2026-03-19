FROM python:3.12-slim

WORKDIR /app

COPY app.py ./
COPY templates ./templates

EXPOSE 8000

ENV HOST=0.0.0.0
ENV PORT=8000

CMD ["python", "app.py"]
