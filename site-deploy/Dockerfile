# ===============================================
# python build stage
FROM python:3.8-alpine3.11 as build

RUN apk add -U gcc g++ musl-dev zlib-dev libuv libffi-dev make openssl-dev git

RUN pip install -U pip setuptools
ADD ./requirements.txt /home/root/requirements.txt
RUN pip install -r /home/root/requirements.txt
# get rid of unnecessary files to keep the size of site-packages and the final image down
RUN find /usr \
    -name '*.py[codxi]' -o \
    -name '*.pxd' -o \
    -name '*.c' -o \
    -name '*.h' -o \
    -name '*.txt' | xargs rm
RUN find /usr -name '__pycache__' -delete
RUN find /usr -name '*.dist-info'  | xargs rm -r

# ===============================================
# final image
FROM python:3.8-alpine3.11

#COPY --from=build /lib/* /lib/
COPY --from=build /usr/lib/* /usr/lib/
COPY --from=build /usr/local/lib/python3.8/site-packages /usr/local/lib/python3.8/site-packages

WORKDIR /home/root/

# could exclude some files, but would it actually save any space in the image?
ADD ./ /home/root/deploy/
ARG COMMIT
ARG BUILD_TIME
ENV PYTHONUNBUFFERED=1 \
    ON_DOCKER=1 \
    COMMIT=$COMMIT \
    BUILD_TIME=$BUILD_TIME

CMD ["uvicorn", "deploy.main:app"]
