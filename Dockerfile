FROM apache/airflow:2.4.2
COPY /requirements/ /requirements/
RUN pip install --user --upgrade pip
RUN pip install --no-cache-dir --user -r /requirements/development.txt