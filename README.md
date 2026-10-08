
# Summer-Quantum-Research
Research repository for my 2026 mentored project comparing quantum oracle sketching (QOS) with classical machine learning methods for DNA promoter sequence classification, with a focus on memory use.

## Project Overview

I completed this project during the summer after my junior year under the wonderful mentorship of the Chicago Infleqtion staff. My project aimed to answer the research question  **how does the memory required by QOS compare with the memory required by classical SVC and SGD classifiers when classifying promoter vs. non-promoter DNA sequences?**

The QOS approach comes from Zhao et al., *"Exponential Quantum Advantage in Processing Massive Classical Data"* (see [References](#references)). It claims that the QOS offers an exponential advantage when processing large data sets, evading the data loading bottleneck that typically happens when using classical methods. 

## Key Findings

- QOS needed only 42 qubits to classify the data compared to the 256 bits needed by the SGD and the 1,000,000+ bits needed by the SVC
- QOS is a much more memory-efficient way to do genomic  data classification 


The full write-up is in [MTendong Quantum Advantage in Classification.pdf](https://github.com/user-attachments/files/33183219/MTendong.Quantum.Advantage.in.Classification.pdf)


## Methodological Note

The classical results (SVC and SGD) are empirical measurements that I was actually able to synthesize within the code. The QOS results are **analytical estimates** that came from the memory-scaling formula in Zhao et al.'s qos.py file, not direct empirical measurements. The comparison should be read with that distinction in mind.

## Focus Areas

- **Quantum-inspired/analytical methods:** QOS memory-scaling analysis compared against classical baselines
- **Genomics:** DNA promoter sequence classification
- **Classical ML baselines:** SVC and SGD classifiers
  
## Tech Stack & Dependencies

* **Language:** Python 3.9+
* **Quantum & Numerical:** JAX, NumPy
* **Data & Machine Learning:** pandas, scikit-learn
* **Visualization:** matplotlib

## References

Zhao et al. (2026). *Exponential quantum advantage in processing massive classical data* https://arxiv.org/abs/2604.07639

## Repository Structure

```text
├── week 1 notes/                       # Initial progress logs and research notes
├── week 2 notes/
│   ├── Blog-post-notes.md              # Blog post that was easy to read, recommended by mentor, has my takeaways & draft outlines
│   ├── mini_reproduction.ipynb         # Small-scale reproduction experiments from the Zhao et al. experiment I am replicating 
│   └── random_sample_Jax.ipynb           
├── week 3/                            
├── numpynotes/                         # Np reference & scratchpad
├── GenomicSequenceClassification.ipynb # Primary research notebook (my figures and project benchmark goals)
├── random_sample_Jax.ipynb             # High-performance JAX circuit sampling script
└── README.md                           # Repository documentation
