# SuperCheQ Notes

**Date:** 05/28/26

## Research Question

Can a quantum computer (QC) create dramatically smaller fingerprints than a classical approach?

---

## Fingerprinting

A **fingerprint** is a compact summary of a file that is unique enough to determine whether two files match.

### Purpose

- Reduce the amount of data that must be compared.
- Determine whether two files are identical using only their fingerprints.

---

## SMP (Simultaneous Message Passing)

A communication model used to:

- Create fingerprints that are as small as possible.
- Compare fingerprints efficiently.
- Determine whether two files are identical.

---

## SuperCheQ

### SuperCheQ-EE (Efficient Encoding)

**Goal:** Maximize compression and fingerprint efficiency.

**Advantages:**
- Provides an exponential advantage over classical methods.

**Challenges:**
- Difficult to implement perfectly on current quantum hardware.

---

### SuperCheQ-IE (Incremental Encoding)

**Goal:** Support efficient updates to fingerprints.

**Advantages:**
- Allows incremental updates.
- Eliminates the need to recompute the entire fingerprint after small changes.
- More practical for current quantum computers.

---

## Noise Testing on Quantum Computers

Quantum hardware is affected by several types of noise:

### Pauli Noise

- Random bit-flip and phase errors.
- One of the most common forms of quantum noise.

### Thermal Noise

- Qubits lose information (decay) over time.

### Coherent Noise

- Systematic errors caused by operations being over- or under-performed.
- Often occurs during quantum gate rotations.

---

## Practical Findings

- Hardware noise remains a major obstacle for modern quantum computers.
- SuperCheQ-IE is currently the most practical approach.
- Requires relatively simple quantum circuits.
- Supports fast and efficient fingerprint updates.

---

## GPU Background

### GPU (Graphics Processing Unit)

A specialized processor designed for highly parallel computations.

**Characteristics:**

- Handles many independent tasks simultaneously.
- Well-suited for floating-point operations.
- Commonly used in scientific computing, machine learning, and simulations.

---

## Key Takeaways

1. Quantum fingerprinting can create much smaller data summaries than classical methods.
2. SMP enables efficient fingerprint comparison.
3. SuperCheQ-EE offers the greatest theoretical advantage but is difficult to implement.
4. SuperCheQ-IE is more practical on today's quantum hardware.
5. Quantum noise remains a significant challenge for real-world deployment.
