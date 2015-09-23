# base
FROM index.alauda.cn/library/ubuntu:14.04


# author
MAINTAINER Julia Jia <juliajia@malongtech.cn>


# update apt-get
COPY sources.list /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y


# use douban pypi
RUN apt-get install -y python-pip
RUN pip install --upgrade pip
COPY pip.conf .pip/pip.conf


# install flask
RUN mkdir /usr/local/src/crawled-item-web
RUN pip install flask
RUN pip install pymongo


# install crawled_item_web.py
RUN mkdir /usr/local/src/crawled-item-web/app
RUN mkdir /usr/local/src/crawled-item-web/app/templates
COPY run.py /usr/local/src/crawled-item-web/
COPY crawled_item_web.py /usr/local/src/crawled-item-web/app/
COPY json.html /usr/local/src/crawled-item-web/app/templates/
COPY base.html /usr/local/src/crawled-item-web/app/templates/
COPY __init__.py /usr/local/src/crawled-item-web/app/
COPY index.html /usr/local/src/crawled-item-web/app/templates/
COPY search.html /usr/local/src/crawled-item-web/app/templates/






# expose port 5000
EXPOSE 5000


