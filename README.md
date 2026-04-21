# DigitalDNA

DigitalDNA is a bio-inspired machine learning framework that encodes features as DNA sequences (A, C, T, G) and applies epigenetic modulation for context-aware predictions.

---

## 🧠 Core Idea

Instead of numeric feature weights, DigitalDNA uses:

* **A, C, T, G** as learnable weights
* A sequence = your input data
* Epigenetics = external/environmental modifiers

---

## ⚙️ Installation

```bash
pip install numpy scipy
```

---

## 🚀 How to Use DigitalDNA on Your Own Data

### Step 1 — Encode your data as sequences

You must convert your features into a DNA-like sequence.

Example:

```python
def encode_example(feature1, feature2, feature3):
    f1 = 'A' if feature1 < 10 else 'C' if feature1 < 20 else 'T' if feature1 < 30 else 'G'
    f2 = 'A' if feature2 < 5 else 'C' if feature2 < 10 else 'T' if feature2 < 15 else 'G'
    f3 = 'A' if feature3 == 0 else 'G'
    return f1 + f2 + f3
```

👉 The rule:

* Each feature → 4 discrete levels → A/C/T/G

---

### Step 2 — Prepare training data

```python
sequences = [
    "ACT",
    "GTA",
    "CCC"
]

labels = [1, 0, 1]  # your target outputs

epigenetics = [
    {'sun_exposure':0.5},
    {'sun_exposure':0.2},
    {'sun_exposure':0.8}
]
```

---

### Step 3 — Train the model

```python
from digitaldna import train

params = train(sequences, labels, epigenetics)
print(params)
```

---

### Step 4 — Make predictions

```python
from digitaldna import model_predict_probability

seq = "ACT"
epi = {'sun_exposure':0.6}

prob = model_predict_probability(seq, params, epi)
print(prob)
```

---

## 🌍 What “Epigenetics” Means in Practice

Epigenetic inputs let you adjust predictions based on context.

Example:

```python
epi = {
    'sun_exposure': 0.7,
    'nutrition': 0.8,
    'stress': 0.2
}
```

You can:

* ignore them (set to 0)
* or redefine them for your domain

---

## 🧪 Example Use Cases

* Astrobiology (planet habitability)
* Weather prediction
* Financial risk scoring
* Health risk modeling
* Any dataset where:

  * features can be discretized into 4 levels
  * environment/context matters

---

## 📁 Project Structure

```
digitaldna.ipynb   # core framework
main.py         # your implementation
README.md
```

---

## ⚠️ Important Notes

* You MUST define your own encoding strategy
* Model performance depends heavily on how you map features → A/C/T/G
* Epigenetic factors are optional but powerful

---

## 📜 License

MIT
