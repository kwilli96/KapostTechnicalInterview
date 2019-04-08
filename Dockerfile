FROM python:latest

ADD CopyFileGreaterThen.py /

RUN pip install boto3

ENV DestBucket "destinationbucketwilkins30"
ENV SrcBucket "sourcebucketwilkins30"
ENV MinSize .02

ENV username AKIAWNAVMEGVNWWFY54Y
ENV passkey r5MRRcbPf5CA3srRoxW0DTN7DwIKMNMhPJqVher4

CMD ["python", "CopyFileGreaterThen.py"]

