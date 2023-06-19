FROM python:3 
RUN pip install kafka-python
RUN pip install pymongo
CMD [ "bash", "-c", "sleep 10 && python -u /consumer.py"]

