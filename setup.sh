#!/bin/bash
# A simple script to set up the test environment for
# the RHEL7 node testers. Load required modules
module load anaconda3/2019.10

# Create the conda environment
echo "Creating python_gnu_parallel environment"
conda env create -f environment.yml

# Activate the environment and collect the path to
# the python interpreter
conda activate python_gnu_parallel
ENV_PYTHON_PATH=$(command -v python)

# Set up executables
if [ ! -d ${PWD}/bin ]; then
    mkdir -p ${PWD}/bin
fi

# Set up analysis
tac ${PWD}/src/analysis.py > /tmp/analysis_tmp && \
    echo -e '#!'${ENV_PYTHON_PATH} >> /tmp/analysis_tmp && \
    tac /tmp/analysis_tmp > ${PWD}/bin/analysis && \
    chmod +x ${PWD}/bin/analysis

# Set up fakedatagen
tac ${PWD}/src/fakedatagen.py > /tmp/fakedatagen_tmp && \
    echo -e '#!'${ENV_PYTHON_PATH} >> /tmp/fakedatagen_tmp && \
    tac /tmp/fakedatagen_tmp > ${PWD}/bin/fakedatagen && \
    chmod +x ${PWD}/bin/fakedatagen

# Set up fragmentor
tac ${PWD}/src/fragmentor.py > /tmp/fragmentor_tmp && \
    echo -e '#!'${ENV_PYTHON_PATH} >> /tmp/fragmentor_tmp && \
    tac /tmp/fragmentor_tmp > ${PWD}/bin/fragmentor && \
    chmod +x ${PWD}/bin/fragmentor

# Set up graphgen
tac ${PWD}/src/graphgen.py > /tmp/graphgen_tmp && \
    echo -e '#!'${ENV_PYTHON_PATH} >> /tmp/graphgen_tmp && \
    tac /tmp/graphgen_tmp > ${PWD}/bin/graphgen && \
    chmod +x ${PWD}/bin/graphgen

# Test that the executables work
cd ${PWD}/bin
if [[ -x analysis && -x fakedatagen && -x fragmentor && -x graphgen ]]; then
    echo "Executables are working"
    echo -e "Please the following command in order to use them:\n"
    echo 'export PATH=${HOME}/work/python_gnu_parallel_test_aci/bin:${PATH}'
    echo -e "\nAll done!"

else
    echo "Something went wrong setting up the executables"
    echo "Please contact Jason at the i-ASK center for help"
fi
