# Build stage
FROM python:3.8.2-slim-buster AS pip
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc
RUN pip install --user --no-warn-script-location numpy matplotlib

# Executable stage
FROM python:3.8.2-alpine3.11
COPY --from=pip /root/.local /root/.local
ENV PATH=/root/.local/bin:$PATH
