FROM python:3.10 as python-base

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt

FROM python-base as shark-unit-test
ENTRYPOINT ["/bin/bash"]
# CMD ["python", "test.py"]

FROM python-base as shark-ui-test
ENTRYPOINT ["/bin/bash"]
# CMD ["app.py"]

# From python-base as shark-deploy
# ENTRYPOINT ["python"]
# CMD ["main.py"]