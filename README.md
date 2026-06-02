<img width="752" height="634" alt="image" src="https://github.com/user-attachments/assets/93aed3ec-a880-442c-b76c-69f05e9e0f0e" />

# BTK 2004 Cipher Visualization & Analysis

A Python visualization and reconstruction project examining the 2004 **BTK ("Bind, Torture, Kill") coded message** attributed to Dennis Rader.

This project recreates the reported **5×5 matrix method**, visualizes coordinate traversal using **color-coded grouping and path rendering**, and documents a proposed reconstruction workflow used to derive the known solution.

---

## Overview

Features:

* 5×5 keyword matrix generation
* coordinate mapping system
* color-grouped traversal visualization
* arrow-based path rendering
* Polybius-style alphabet matrix comparison
* reconstruction notes and uncertainty analysis

---

## Background

In 2004, Dennis Rader mailed investigators a coded communication alongside:

* Vicki Wegerle’s driver's license
* crime scene photographs
* material confirming responsibility for her 1986 murder

The homicide had remained disputed for approximately 18 years, with suspicion often directed toward Wegerle’s husband.

The ciphertext supplied by Rader was:

```text
GBSOAP7-TNLTRDEITBSFAV14
```

Following Rader’s 2005 arrest, investigators questioned him regarding the encoding method.

According to public reporting and later discussion, Rader stated:

* the system resembled a **"German fractional code"**
* a **keyword** was required
* he associated the method with Air Force training
* he was unable to fully reconstruct his exact encoding process

The reported keyword:

```text
PIANO
```

"PIANO" was allegedly used by Rader as a stalking project name for **Vicki Wegerle**.

---

## Known Proposed Solution

Publicly discussed reconstruction produced:

```text
VAGIAN7-LETBEATTIEKNOW14
```

The second section:

```text
LET BEATTIE KNOW
```

is generally interpreted as referring to Wichita attorney **Robert Beattie**, who was preparing a BTK case book.

The first section:

```text
VAGIAN7
```

is commonly interpreted as:

```text
VAGINA7
```

Possible explanations:

1. spelling error by Rader
2. encoding / transcription mistake
3. incomplete reconstruction of the original cipher method

Numeric suffixes remain uncertain:

```text
7
14
```

Interpretations proposed by researchers include:

* 7 known BTK victims at the time
* implication of additional victims
* internal numbering system
* symbolic taunt
* incomplete or misleading communication

Rader later confessed to **10 murders**.

---

## Matrix Construction

The reconstruction combines:

```text
Keyword + Ciphertext
```

Input:

```text
Keyword:
PIANO

Cipher:
GBSOAP7TNLTRDEITBSFAV14
```

Generated matrix:

```text
P I A N O
G B S O A
P T N L T
R D E I T
B S F A V
```

---

## Coordinate System

Coordinates use:

```text
(row,column)
```

with **1-indexed notation**.

Example:

```text
P = (1,1)
I = (1,2)
A = (1,3)
N = (1,4)
O = (1,5)
```

Full coordinate map:

```text
(1,1) P   (1,2) I   (1,3) A   (1,4) N   (1,5) O
(2,1) G   (2,2) B   (2,3) S   (2,4) O   (2,5) A
(3,1) P   (3,2) T   (3,3) N   (3,4) L   (3,5) T
(4,1) R   (4,2) D   (4,3) E   (4,4) I   (4,5) T
(5,1) B   (5,2) S   (5,3) F   (5,4) A   (5,5) V
```

---

## Coordinate Traversal Sequence

Proposed traversal order:

```text
(1,3) (2,5) (5,3) (2,2) (5,2)
(4,1) (4,2) (5,4) (2,1) (1,2)
(4,3) (3,4) (1,4) (3,3) (1,5)
(2,4) (1,1) (3,1) (2,3) (4,5)
(3,2) (3,5) (4,4) (5,5) (5,1)
```

This sequence appears to behave as a **coordinate permutation / traversal ordering system**.

The exact original derivation remains undocumented and uncertain.

---

## Alphabet Matrix

Reconstruction compares the traversal against a standard **Polybius-style 5×5 alphabet matrix**.

```text
A B C D E
F G H I/J K
L M N O P
Q R S T U
V W X Y Z
```

Coordinate form:

```text
(1,1)=A   (1,2)=B   (1,3)=C   (1,4)=D   (1,5)=E
(2,1)=F   (2,2)=G   (2,3)=H   (2,4)=I/J (2,5)=K
(3,1)=L   (3,2)=M   (3,3)=N   (3,4)=O   (3,5)=P
(4,1)=Q   (4,2)=R   (4,3)=S   (4,4)=T   (4,5)=U
(5,1)=V   (5,2)=W   (5,3)=X   (5,4)=Y   (5,5)=Z
```

This resembles:

* Polybius square
* fractional substitution systems
* coordinate-based cipher encoding

---

## Visualization Features

The program renders:

### Matrix Generation

Automatic creation of:

```text
keyword + ciphertext → 5×5 matrix
```

### Coordinate Traversal

Displays:

* coordinate order
* traversal numbering
* traversal sequence

### Color-Grouped Analysis

Coordinates divided into **5 colored groups**.

| Group | Color  |
| ----- | ------ |
| 1     | Red    |
| 2     | Blue   |
| 3     | Green  |
| 4     | Orange |
| 5     | Purple |

### Path Visualization

Arrow rendering connects sequential traversal coordinates.

Useful for examining:

* permutation behavior
* traversal structure
* coordinate grouping
* reconstruction hypotheses

---

## Project Structure

```text
.
├── solve_btk.py
├── requirements.txt
├── README.md
└── examples/
    └── visualization.png
```

---

## Installation

### Create requirements file

`requirements.txt`

```txt
numpy
matplotlib
```

### Standard Installation

```bash
python -m pip install -r requirements.txt
```

### Managed / uv / PEP-668 Environments

Create a virtual environment:

```bash
python -m venv venv
```

Git Bash:

```bash
source venv/Scripts/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run

```bash
python solve_btk.py
```

---

## Example Output

Program output includes:

* generated matrix
* colored coordinate groups
* numbered traversal
* directional arrows
* cipher path visualization

Add screenshot example:

```text
examples/visualization.png
```

---

## Sources & Credits

### Primary Discussion Source

Reddit discussion:

**BTK Codes — r/ZodiacKiller**

https://www.reddit.com/r/ZodiacKiller/comments/egk6dp/btk_codes/

Discussion topics include:

* BTK coded communications
* PIANO keyword usage
* 5×5 matrix reconstruction
* coordinate ordering concepts
* Zodiac-style cipher comparisons

### Special Thanks

**David Oranchak**

YouTube:

https://www.youtube.com/watch?v=HqB-fUuMUxs

Recognition for educational work on historical cipher analysis and Zodiac cryptography research.

---

## Notes

Several aspects of the BTK reconstruction remain unresolved.

Open questions include:

* exact encoding mechanism
* traversal derivation logic
* numeric suffix interpretation
* intended meaning of "14"
* "VAGIAN" vs "VAGINA"

This repository presents a **research / visualization reconstruction**, not a definitive forensic decoding.

---

## Disclaimer

Repository purpose:

* cryptography education
* visualization research
* historical cipher analysis
* programming experimentation

No endorsement, glorification, or celebration of criminal acts or offenders is intended.

Subject matter is discussed strictly for historical and cryptographic analysis.

---

## License

MIT License
