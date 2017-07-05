FROM kernsuite/base:2
RUN docker-apt-install python-casacore python-tk
ADD . /build
RUN pip install /build
