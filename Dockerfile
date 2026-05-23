
COREX v1.0.0

Causal Origin Resolution and Empirical eXamination

FROM python:3.11-slim

WORKDIR /app

Install system dependencies

RUN apt-get update && apt-get install -y 
    gcc 
    g++ 
    && rm -rf /var/lib/apt/lists/*

Copy requirements and install Python dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

Copy source code

COPY corex/ ./corex/
COPY configs/ ./configs/
COPY data/ ./data/

Set environment variables

ENV COREX_LOG_LEVEL=INFO
ENV COREX_SAVE_REPORT=true
ENV COREX_REPORT_DIR=/app/reports

Create output directory

RUN mkdir -p /app/reports

Default command

CMD ["python", "-c", "from corex import version; print(f'COREX v{version} ready')"]
