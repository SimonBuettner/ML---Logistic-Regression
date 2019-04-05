FROM python
ADD . /myapp
WORKDIR /myapp
RUN pip install -r requirements.txt
ENTRYPOINT [ "python", "chuck.py" ]