# Read in ubuntu based docker image
FROM ubuntu:20.04

#Environment
ENV 
ENV

# Install needed UBUNTU packages
RUN apt-get update && \
    apt-get install -y curl git

# Install python 3.8.3 version of miniconda
RUN echo "Installing miniconda ..." && \
    curl -sSLO https://repo.anaconda.com/miniconda/Miniconda-3.8.3-Linux-x86_64.sh && \
    bash Miniconda-3.8.3-Linux-x86_64.sh -b -p /usr/local/miniconda && \
    rm Miniconda-3.8.3-Linux-x86_64.sh 

# create conda environment
RUN conda create -n torch_cudnn8.2 python=3.8.3
# Install Dependencies
SHELL ["conda", "run", "-n", "torch_cudnn8.2 ", "conda", "install", "-y" "pip", "numpy", "ninja", "pyyaml", "mkl", "mkl-include", "setuptools", "cmake", "cffi", "typing_extensions", "future", "six", "requests", "dataclasses"]
SHELL ["conda", "run", "-n", "torch_cudnn8.2 ", "conda", "install", "-y", "--channel", "pytorch", "magma-cuda112"]

# download pytorch repo
RUN mkdir github && \
    cd github && \
    git clone --recursive https://github.com/pytorch/pytorch && \
    cd pytorch && \
    /usr/local/miniconda/envs/torch_cudnn8.2/bin/python ./setup.py install

# copy files from outside to inside docker image
#COPY run.py /run.py
#COPY heuristics /heuristics
#COPY IntendedFor.py /IntendedFor.py

#ENTRYPOINT ["/usr/local/miniconda/envs/torch_cudnn8.2/bin/python", "/run.py"]

# placeholders
"""
mamba create -n torch_cudnn8.2

source activate torch_cudnn8.2
if [[ $! != 0 ]]; then
        echo "torch_cudnn8.2 not activated"
else
        echo "torch_cudnn8.2 activated"
fi

mamba install -y numpy ninja pyyaml mkl mkl-include setuptools cmake cffi typing_extensions future six requests dataclasses
mamba install -y --channel pytorch magma-cuda112

cd /home/support/lamx0031/My_Tutorial/PyTorch/torch_src
mkdir pytorch_src
cd pytorch_src

git clone --recursive https://github.com/pytorch/pytorch
cd pytorch
export CMAKE_PREFIX_PATH=${CONDA_PREFIX:-"$(dirname $(which conda))/../"}
export CUDNN_LIB_DIR=/panfs/roc/msisoft/cudnn/8.2.0/lib64
export CUDNN_INCLUDE_DIR=/panfs/roc/msisoft/cudnn/8.2.0/include
export CUDNN_LIBRARY=/panfs/roc/msisoft/cudnn/8.2.0/lib64

#env > env_out
python ./setup.py install
""""