FROM python:3.8

ENV FTS_MAINPATH="/data"
ENV FTS_DOCKER=True
ENV FTS_CONFIG_PATH="/data/FTSConfig.yaml"
ENV FTS_DB_PATH="/data/FTSDataBase.db"

WORKDIR /FreeTAKServer
COPY . .
COPY ./FreeTAKServer /FreeTAKServer

#RUN pip3 install flask lxml flask_login

RUN pip3 install -e /FreeTAKServer

# don't use root, let's not have FTS be used as a priv escalation in the wild
# RUN groupadd -r freetak && useradd -m -r -g freetak freetak
# RUN mkdir /data ; chown -R freetak:freetak /data 
# RUN chown -R freetak:freetak /FreeTAKServer
# USER freetak 

# DataPackagePort
EXPOSE 8080
# CoTPort
EXPOSE 8087
# SSLCoTPort
EXPOSE 8089
# SSLDataPackagePort
EXPOSE 8443
# FederationPort
EXPOSE 9000
# APIPort
EXPOSE 19023

#ENTRYPOINT [ "python", "TAKfreeServer/run.py", "-p", "8087" ]
ENTRYPOINT [ "python3", "-m", "FreeTAKServer.controllers.services.FTS", "-DataPackageIP", "0.0.0.0", "-AutoStart", "True"]