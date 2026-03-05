# Q1 – Turing Test and CAPTCHA

## Problem Statement

Think of how **Turing Test** and **CAPTCHA** could be implemented and suggest an appropriate architecture for their design.

---

## Approach

For this question, the architecture for both systems was designed and documented.  
A working python implementation was provided for the **CAPTCHA system**. 

Please open the architecture design [here](architecture.md) to find a basic overview of the proposed architectures.

- The **Turing Test** section focuses on architectural design and system components.
- The **CAPTCHA system** includes both architecture and a simple Python implementation.

---

## Files

| File | Description |
|-----|-------------|
| `architecture.md` | Architecture and design explanation for Turing Test and CAPTCHA |
| `captcha.py` | Python implementation of a simple CAPTCHA |

---

## CAPTCHA Implementation

The CAPTCHA system generates a random 5-character code consisting of letters and digits.  
To achieve the purpose of a CAPTCHA, random noise symbols such as !, | and * are added inbetween the characters.

The system allows **3 attempts** to enter the correct CAPTCHA. If the user fails to guess it within **3 attempts**, the program exits assuming a bot was on the other end.

---

## Running the Program

Run the CAPTCHA program using:

```bash
python captcha.py

--- CAPTCHA Verification ---

[ A* B| 3~ T! K. ]
Enter the 5 characters shown in the CAPTCHA (without spaces):
