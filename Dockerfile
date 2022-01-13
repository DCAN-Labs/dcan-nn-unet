# Use Ubuntu 20.04 LTS
FROM ubuntu:focal-20210416

# Prepare environment
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
                    apt-utils \
                    autoconf \
                    build-essential \
                    bzip2 \
                    ca-certificates \
                    curl \
                    gcc \
                    git \
                    gnupg \
                    libtool \
                    lsb-release \
                    pkg-config \
                    unzip \
                    wget \
                    xvfb && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/
RUN wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
RUN mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
RUN wget https://developer.download.nvidia.com/compute/cuda/11.6.0/local_installers/cuda-repo-ubuntu2004-11-6-local_11.6.0-510.39.01-1_amd64.deb
RUN dpkg -i cuda-repo-ubuntu2004-11-6-local_11.6.0-510.39.01-1_amd64.deb
RUN apt-key add /var/cuda-repo-ubuntu2004-11-6-local/7fa2af80.pub
RUN apt-get update && \
    apt-get -y install cuda

#RUN wget https://developer.nvidia.com/compute/cudnn/secure/8.3.2/local_installers/10.2/cudnn-linux-x86_64-8.3.2.44_cuda10.2-archive.tar.xz
# Create a shared $HOME directory
#RUN useradd -m -s /bin/bash -G users bibsnet
#WORKDIR /home/bibsnet
#ENV HOME="/home/bibsnet" \
#    LD_LIBRARY_PATH="/usr/lib/x86_64-linux-gnu:$LD_LIBRARY_PATH"
# Install python 3.8.3 version of miniconda
#RUN echo "Installing miniconda ..." && \
#    curl -sSLO https://repo.anaconda.com/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh && \
#    bash Miniconda3-py38_4.10.3-Linux-x86_64.sh -b -p /usr/local/miniconda && \
#    rm Miniconda3-py38_4.10.3-Linux-x86_64.sh 
#RUN ln -s /usr/local/miniconda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
#    echo ". /usr/local/miniconda/etc/profile.d/conda.sh" >> ~/.bashrc && \
#    echo "conda activate base" >> ~/.bashrc
#RUN echo ". /usr/local/miniconda/etc/profile.d/conda.sh" >> $HOME/.bashrc && \
#    echo "conda activate base" >> $HOME/.bashrc
# create conda environment
#ENV PATH=$PATH:/usr/local/miniconda/condabin:/usr/local/miniconda/bin \
#    CPATH="/usr/local/miniconda/include:$CPATH" \
#    LD_LIBRARY_PATH="/usr/local/miniconda/lib:$LD_LIBRARY_PATH" \
#    LANG="C.UTF-8" \
#    LC_ALL="C.UTF-8" \
#    PYTHONNOUSERSITE=1
#RUN conda install -y pip numpy ninja pyyaml mkl setuptools cmake cffi future six requests
#RUN conda install -y --channel pytorch magma-cuda112

# download pytorch repo
#RUN mkdir github && \
#    cd github && \
#    git clone --recursive https://github.com/pytorch/pytorch && \
#    cd pytorch
#WORKDIR pytorch
#RUN /usr/local/miniconda/bin/python setup.py install
