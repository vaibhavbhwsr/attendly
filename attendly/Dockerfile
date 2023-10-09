FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

WORKDIR /attendly

COPY . /attendly/

RUN pip install --upgrade pip
RUN pip install -r requirements.dev.txt

RUN sed -i 's/\r$//g' /attendly/entrypoint.sh
RUN chmod +x /attendly/entrypoint.sh

# run entrypoint.sh
ENTRYPOINT ["/attendly/entrypoint.sh"]