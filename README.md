# Genome Epidemiology 1 - NGS: Spring 2023

This repository contains the code used in the Next Generation Sequencing (NGS) section of the Genome Epidemiology 1 course for Spring 2023. We're working with Whole Genome Sequencing (WGS) data of Mycobacterium tuberculosis samples retrieved from the NCBI database.

## Content

The main code notebooks are as follows:

1. **1-Dataset.ipynb**: Downloading the dataset from the NCBI database.
2. **2-QC.ipynb**: Checking the basic information of sequence data with `FastQC` and performing read trimming with `Trimmomatic`.
3. **3-Alignment.ipynb**: Performing sequence alignment using `BWA-MEM`.
4. **4-CallVariants.ipynb**: Performing multi-sample variant calling with `bcftools`, processing the genome in chunks.

## Requirements

- `conda`
- `python3`

## Package Installation

### Conda Packages

To install the required conda packages, you can update your current environment:
```bash
conda env update --file conda_env.yaml
```
Or you can create a new conda environment:
```bash
conda env create -f conda_env.yaml -n tools
```

### Python Packages

To install the required Python packages, you can use pip:
```bash
pip install -r requirements.txt
```
