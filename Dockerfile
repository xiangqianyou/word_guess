FROM python:3.9-alpine

WORKDIR /word_guess

COPY . /word_guess

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]