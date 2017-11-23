FROM kernsuite/base:3
RUN docker-apt-install python-casacore python-tk python-pip
ADD . /build
RUN pip install /build
