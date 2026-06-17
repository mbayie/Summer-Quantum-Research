# Linear Support Vector Machines (SVM)

## Overview

**Support Vector Machine (SVM)** is a supervised machine learning algorithm used for:

- Classification tasks
- Regression tasks

The primary goal of an SVM is to find a decision boundary that separates data into different classes.

---

## Hyperplane

### Definition

A **hyperplane** is a flat geometric boundary that separates a dataset into different classes.

More formally:

- A hyperplane has one fewer dimension than the space in which it exists.
- In two dimensions, a hyperplane is a line.
- In three dimensions, a hyperplane is a plane.
- In higher dimensions, it is a generalized decision boundary.

### Purpose

The SVM finds the hyperplane that best separates the dataset into two classes.

---

## Margin

### Definition

The **margin** is the distance between the hyperplane and the nearest data points from either class.

### Importance

A good SVM aims to maximize the margin because:

- Larger margins generally improve generalization.
- The classifier becomes more robust to new data.
- The risk of overfitting is reduced.

---

## Linear SVM

### When It Works

A **Linear SVM** is used when the data is **linearly separable**.

This means:

- The classes can be separated using a straight line (2D).
- Or a flat hyperplane (higher dimensions).

### Characteristics

- Simple and computationally efficient.
- Works well when classes are clearly separated.
- Produces a single optimal separating hyperplane.

Example:

```text
Class A      |      Class B
○ ○ ○ ○      |      △ △ △ △
○ ○ ○ ○      |      △ △ △ △
```

---

## Nonlinear Data

### The Problem

Sometimes data cannot be separated using a straight line or flat hyperplane.

Example:

```text
      △ △ △
    △     △
      ○ ○
    ○     ○
      ○ ○
```

No single straight line can separate the classes.

### Solution

The data can be transformed into a higher-dimensional space where it becomes linearly separable.

For example:

- Two-dimensional data may be mapped into three dimensions.
- A nonlinear boundary in 2D can become a linear hyperplane in 3D.

This idea forms the basis of kernel methods used in SVMs.

---

## Linear vs. Nonlinear SVM

| Linear SVM | Nonlinear SVM |
|------------|---------------|
| Data is linearly separable | Data is not linearly separable |
| Uses a straight-line boundary | Uses transformed feature space |
| Faster and simpler | More flexible and powerful |
| Lower computational cost | Higher computational cost |

---

## Key Takeaways

1. SVMs are used for both classification and regression.
2. The goal is to find the optimal hyperplane separating classes.
3. The margin measures how far the nearest points are from the hyperplane.
4. Maximizing the margin generally improves model performance.
5. Linear SVMs work when data is linearly separable.
6. Nonlinear problems can often be solved by transforming data into a higher-dimensional space.
