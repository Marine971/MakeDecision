FROM python:3.9

ADD main.py .

RUN pip install requests beautifulsoup4
RUN <<EOF \main
print("y") \
EOF

CMD ["python", "./main.py"]