# GeneWeaver — GPU-Accelerated CRISPR Alignment Engine

Educational Python prototype for local DNA sequence alignment and candidate SpCas9 guide/PAM discovery.

## Features
- FASTA parsing and sequence input
- Smith–Waterman local alignment (CPU reference implementation)
- Optional CUDA environment detection with safe CPU fallback
- Detection of 20-nt guide sequences immediately upstream of an NGG PAM
- Streamlit interface and tabular results

## Setup
1. Install Python 3.10+.
2. Create and activate a virtual environment.
3. Install dependencies: `pip install -r requirements.txt`
4. Run: `streamlit run app.py`

## Important GPU note
The project includes optional Numba CUDA detection, but the supplied version intentionally uses a validated CPU implementation as the correctness baseline. A true GPU implementation requires a carefully tested anti-diagonal/wavefront CUDA kernel and compatible NVIDIA CUDA hardware/drivers. Do not describe this starter build as having measured GPU acceleration.

## Sample input
>query
ACGTACGTACGTACGTACGT
>reference
TTTACGTACGTACGTACGTACGTAAA

## Limitations and responsible use
This is a learning/demo tool, not a clinical decision-support system. PAM matches are preliminary candidates, not proof of editing efficiency or safety. It does not perform genome-wide off-target analysis, variant interpretation, guide efficacy prediction, or laboratory validation. Use curated reference genomes and validated tools for research workflows.
