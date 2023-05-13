# Genome Epidemiology 1 - NGS: Spring 2023

This repository contains the code used in the Next Generation Sequencing (NGS) section of the Genome Epidemiology 1 course for Spring 2023. We're working with Whole Genome Sequencing (WGS) data of Mycobacterium tuberculosis samples retrieved from the NCBI database.

## Contents

The main code notebooks are as follows:

1. **1-Dataset.ipynb**: Downloading the dataset from the NCBI database.
  ```mermaid
  flowchart LR
    D1[("<i>NCBI</i> database")]
    D2("Raw reads(<i>FASTQ</i>)")

    D1 -- "Fetch" --> D2
  ```
2. **2-QC.ipynb**: Checking the basic information of sequence data with `FastQC` and performing read trimming with `Trimmomatic`.
  ```mermaid
  flowchart LR
    D1("Raw reads\n(<i>FASTQ</i>)")
    D2("Trimmed reads\n(<i>FASTQ</i>)")

    
    T1{<i>Trimmomtaic</i>}
    T2{FastQC}

    
    D1 --- T2
    T2 -- "Overview" --> D3("Reports\n(<i>html</i>)")
    D1 --- T1
    T1 -- "Trimming" --> D2
  ```
3. **3-Alignment.ipynb**: Performing sequence alignment using `BWA-MEM`.
  ```mermaid
  flowchart LR
    D1("Reference genome\n(<i>FASTA</i>)")
    D2("Trimmed reads\n(<i>FASTQ</i>)")
    D3("Alignment map\n(<i>SAM</i>)")
    D4("Sorted binary\n(<i>BAM</i>)")

    T1{<i>BWA</i>}
    T2{<i>Samtools</i>}

    T1 -. "Indexing" .-> D1
    D1 --> T1
    D2 --> T1
    T1 -- "Mapping" --> D3
    D3 --> T2
    T2 -- "Sorting\nCompressing" --> D4
  ```
4. **4-CallVariants.ipynb**: Performing multi-sample variant calling with `bcftools`, processing the genome in chunks.
  ```mermaid
  flowchart LR
    D1("Reference genome\n(<i>FASTA</i>)")
    D2[("Multiple alignment maps\n(<i>BAM</i>)")]

    D3("Callset in region\n(<i>vcf</i>)")
    D4[("Multiple callsets\n(<i>vcf</i>)")]
    D5("Merged callsets\n(<i>vcf</i>)")
    
    T1{<i>bcftools</i>}
    T2{<i>Samtools</i>}
    T3{<i>bcftools</i>}

    T2 -. "Indexing" .-> D2
    D1 -- "Divide into chunks" --> T1
    D2 --- T1
    T1 -- "Pileup\n& Calling" --> D3
    D3 --- T3
    D4 --- T3
    T3 -- "Concatenate\n& Normalize" --> D5
  ```

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
