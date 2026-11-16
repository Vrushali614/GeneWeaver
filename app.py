import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from alignment import align_cpu, align_gpu_optional, find_crispr_targets, parse_fasta

st.set_page_config(page_title="GeneWeaver", page_icon="🧬", layout="wide")
st.title("🧬 GeneWeaver")
st.caption("GPU-Accelerated CRISPR Alignment Engine | Educational research prototype")

with st.sidebar:
    st.header("Input")
    mode = st.radio("Input format", ["Paste sequences", "Upload FASTA"])
    engine = st.selectbox("Alignment engine", ["CPU", "GPU (optional; safe fallback)"])

if mode == "Upload FASTA":
    file = st.file_uploader("Upload FASTA file", type=["fa", "fasta", "fna"])
    raw = file.read().decode("utf-8") if file else ""
else:
    raw = st.text_area("FASTA or raw DNA sequence", value=">query\nACGTACGTACGTACGTACGT\n>reference\nTTTACGTACGTACGTACGTACGTAAA", height=160)

records = parse_fasta(raw) if raw.strip() else []
if len(records) >= 2:
    query_name, query = records[0]
    ref_name, reference = records[1]
    if st.button("Run analysis", type="primary"):
        result = align_cpu(query, reference) if engine == "CPU" else align_gpu_optional(query, reference)
        c1, c2, c3 = st.columns(3)
        c1.metric("Alignment score", result.score)
        c2.metric("Execution time", f"{result.elapsed_seconds*1000:.3f} ms")
        c3.metric("Engine", result.engine)
        st.subheader("Local alignment")
        st.code(f"Query:     {result.aligned_query}\nReference: {result.aligned_reference}")
        st.write(f"Start positions (0-based): query {result.start_query}, reference {result.start_reference}")
        st.subheader("Candidate SpCas9 guide/PAM sites")
        hits = find_crispr_targets(reference)
        if hits:
            st.dataframe(pd.DataFrame(hits), use_container_width=True)
        else:
            st.info("No 20-nt guide followed by an NGG PAM was found in this sample.")
        st.warning("Candidate sites are computational predictions only. Check off-targets and validate independently; do not use this prototype for clinical decisions.")
else:
    st.info("Provide at least two FASTA records: the query sequence first and reference sequence second.")
