FROM python:latest

ADD CopyFileGreaterThen.py /

RUN pip install boto3

ENV username AKIAWNAVMEGVNWWFY54Y
ENV passkey r5MRRcbPf5CA3srRoxW0DTN7DwIKMNMhPJqVher4

ENTRYPOINT ["python", "CopyFileGreaterThen.py"]

