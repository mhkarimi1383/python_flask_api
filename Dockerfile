from python

WORKDIR /python_flask

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

CMD [ "python3", "./restful_api.py" ]
