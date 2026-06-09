# K-mers & Genomics Notes

**Date:** 05/30/26

## GenomeScope

### What is GenomeScope?

GenomeScope is a tool that analyzes patterns in raw DNA sequencing data to estimate important properties of a genome.

### Key Properties Estimated

- **Genome size**
- **Repetitiveness** (how much repeated DNA exists)
- **Heterozygosity** (genetic variation between chromosome copies)

---

## K-mers

### Definition

A **k-mer** is a DNA substring of length *k*.

### Example

For the DNA sequence:

```text
AATTTGACCG
```

The 3-mers are:

```text
AAT, ATT, TTT, TTG, TGA, GAC, ACC, CCG
```

### Why K-mers Matter

Researchers can count how frequently each k-mer appears in sequencing data.

The distribution of these counts reveals information about the underlying genome.

---

## K-mer Frequency Graph

### Purpose

A k-mer graph plots how often each k-mer appears in the sequencing dataset.

### Interpretation

- The graph often forms a bell-shaped distribution.
- The peak indicates the **coverage depth** of the sequencing data.

### Example

If the peak occurs at **25**:

- Most unique k-mers were observed approximately 25 times.
- The sequencing coverage is roughly 25×.

### Sequencing Errors

Sequencing mistakes create:

- Rare k-mers
- Incorrect k-mers
- Additional noise in the graph

These often appear at very low frequencies.

---

## How GenomeScope Interprets the Graph

GenomeScope analyzes the shape of the k-mer frequency distribution to infer genome characteristics.

### Peak Patterns

| Pattern | Interpretation |
|----------|---------------|
| Large peak | Homozygous regions |
| Smaller peak | Heterozygous regions |

### Why This Matters

The relationship between these peaks provides information about:

- Genetic variation
- Genome complexity
- Repetitive content

---

## Applications

Researchers use GenomeScope to estimate:

- Genome size
- Genome repetitiveness
- Genome variability

These estimates are valuable when preparing for **genome assembly** and other downstream genomic analyses.

---

## Key Takeaways

1. K-mers are short DNA sequences of length *k*.
2. Counting k-mer frequencies reveals important properties of a genome.
3. GenomeScope uses k-mer frequency distributions to estimate genome characteristics.
4. Sequencing errors create low-frequency, incorrect k-mers.
5. Peak locations and shapes help identify coverage depth, heterozygosity, and genome complexity.
