# Mr Aegis brain container
# Includes the repository source tree; model weights are loaded at runtime.
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    AEGIS_CHECKPOINT_PATH=Aegis/Aegis-7B-Chat \
    AEGIS_SERVER_HOST=0.0.0.0 \
    AEGIS_SERVER_PORT=8000 \
    AEGIS_CPU_ONLY=1

WORKDIR /opt/mr-aegis

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash git ca-certificates build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install a CPU PyTorch build so the image runs on ordinary Docker hosts.
RUN python -m pip install --upgrade pip \
    && python -m pip install torch==2.2.2 --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt ./requirements.txt
RUN python -m pip install -r requirements.txt

# Bring the complete Mr Aegis repository source into the image.
COPY . .
RUN chmod +x /opt/mr-aegis/docker-entrypoint.sh

EXPOSE 8000
VOLUME ["/models", "/root/.cache/huggingface"]

ENTRYPOINT ["/opt/mr-aegis/docker-entrypoint.sh"]
