Ham believes nnUNet was installed into a conda environment following 
the install steps specified on its website. A batch job was used to build the 
conda environment which has a source-built pytorch that uses cudnn8.2 . 
He would imagine you could use the same install steps for nnUNet in the 
docker file.  He thinks the challenging task would be to correctly layout the pytorch and cudnn compile/build steps in the docker file to complete the image creation since the container needs to have the full software stack to support nnUNet. 

Below is the batch job script that builds pytorch from source:

    #modification needed if adapted for other uses.  
    #!/bin/bash
    #SBATCH --job-name=buildpytorch  # job name
    #SBATCH --nodes=1                # node count
    #SBATCH --ntasks=2               # total number of tasks across all nodes
    #SBATCH --cpus-per-task=1        # cpu-cores per task (>1 if multi-threaded tasks)
    #SBATCH --mem-per-cpu=32G        # memory per cpu-core (what is the default?)
    #SBATCH --time=14:00:00          # total run time limit (HH:MM:SS)
    
    #SBATCH -p v100
    #SBATCH --gres=gpu:v100:1
    
    #SBATCH --mail-type=begin        # send email when job begins
    #SBATCH --mail-type=end          # send email when job ends
    #SBATCH --mail-user=lamx0031@umn.edu
    #SBATCH -e torch_build-%j.err
    #SBATCH -o torch_build-%j.out
    
    
    ## bulid script here
    module load python3/3.8.3_anaconda2020.07_mamba
    module load gcc
    module load cuda/11.2
    module load cudnn/8.2.0
    
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