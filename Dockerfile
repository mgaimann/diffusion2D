FROM python:3
LABEL authors="mgaimann"
WORKDIR /usr/src/app

RUN git clone https://github.com/mgaimann/diffusion2D.git
RUN cd diffusion2D
RUN ls
RUN python -m pip install .

CMD [ "python3", "diffusion2d.py" ]





ENTRYPOINT ["top", "-b"]