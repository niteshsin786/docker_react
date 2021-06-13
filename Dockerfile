FROM python:3
ENV PYTHONUMBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app/
COPY entrypoint.sh /app/
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 8000

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD ["sh", "-c", "tail -f /dev/null"]