FROM python:3.9.5-buster

USER root

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list' \
&& apt update \ 
&& apt install -y google-chrome-stable \
&& python3 -m pip install -U selenium \
&& wget https://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip \
&& unzip chromedriver_linux64.zip \
&& cp chromedriver /usr/local/bin/ \
&& cp chromedriver /usr/bin/

COPY ./WebTest.py WebTest.py
COPY ./WebBuyerTest.py WebBuyerTest.py

RUN python3 WebBuyerTest.py

CMD [ "python3", "WebTest.py" ]