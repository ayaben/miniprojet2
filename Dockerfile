FROM python:3.6

# Import codebase
COPY . /app
WORKDIR /app


RUN pip install folium

CMD ["python","./main.py"]
