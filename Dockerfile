FROM python:latest

ADD CopyFileGreaterThen.py / 
COPY requirements.txt /

RUN pip install -r requirements.txt

ENV username AKIAWNAVMEGVNWWFY54Y
ENV passkey r5MRRcbPf5CA3srRoxW0DTN7DwIKMNMhPJqVher4

ENTRYPOINT ["python", "CopyFileGreaterThen.py"]