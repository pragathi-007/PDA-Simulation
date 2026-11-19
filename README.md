# Beyond Finite Memory: Pushdown Automata Simulation

## Project Overview

This project implements a **Pushdown Automata (PDA) Simulator using Python** to demonstrate how stack memory helps recognize Context-Free Languages (CFLs).

The simulation covers two important applications:

1. Balanced Parentheses Recognition using PDA.
2. Palindrome Recognition using Non-Deterministic Pushdown Automata (NPDA).

## Objectives

- Understand the working of Pushdown Automata.
- Demonstrate PUSH and POP stack operations.
- Simulate balanced parentheses recognition.
- Implement palindrome recognition using NPDA.
- Understand nondeterministic transitions using Breadth-First Search (BFS).
- Display step-by-step simulation traces.

## Technologies Used

- **Programming Language:** Python 3
- **Concepts:** Pushdown Automata, Stack, NPDA, BFS
- **IDE:** Visual Studio Code
- **Version Control:** Git and GitHub

## Project Structure

```text
PDA-Simulation/
│
├── pda_simulator.py
└── README.md
```

## Features

### 1. Balanced Parentheses PDA

The PDA checks whether parentheses are properly balanced.

**Working:**
- PUSH operation when `(` is encountered.
- POP operation when `)` is encountered.
- Accepts if only the bottom stack marker remains after processing the input.
- Rejects unmatched or incorrectly ordered parentheses.

**Example:**

| Input | Result |
|---|---|
| `(()())` | ACCEPTED |
| `(()` | REJECTED |
| `())` | REJECTED |
| `()()` | ACCEPTED |

### 2. Palindrome NPDA

The NPDA recognizes palindromes over the alphabet `{a, b}`.

**Working:**
- Pushes the first half of the input onto the stack.
- Nondeterministically guesses the middle.
- Matches the remaining input with stack symbols.
- Accepts if an accepting branch successfully matches the entire string.

Breadth-First Search (BFS) is used to explore possible configurations.

**Example:**

| Input | Result |
|---|---|
| `abba` | ACCEPTED |
| `aba` | ACCEPTED |
| `aabbaa` | ACCEPTED |
| `abab` | REJECTED |
| `baab` | ACCEPTED |

## How to Run the Project

### Step 1: Install Python

Install Python 3 on your computer.

### Step 2: Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/PDA-Simulation.git
```

### Step 3: Open the Project Folder

```bash
cd PDA-Simulation
```

### Step 4: Run the Program

```bash
python pda_simulator.py
```

## Program Menu

After executing the program, the following menu appears:

```text
==============================================
          PDA SIMULATION PROGRAM
==============================================
1. Balanced Parentheses PDA
2. Palindrome NPDA
3. Run sample test cases
4. Exit
```

Choose an option to perform the required simulation.

## Sample Output

```text
Input: '(()())'
Result: ACCEPTED

Input: '(()'
Result: REJECTED

Input: 'abba'
Result: ACCEPTED

Input: 'abab'
Result: REJECTED
```

## Conclusion

This project demonstrates how Pushdown Automata use stack memory to recognize languages that require more memory than finite automata.

The balanced parentheses PDA demonstrates deterministic stack operations, while the palindrome NPDA demonstrates nondeterministic transitions and BFS-based configuration exploration.

## Academic Details

**Subject:** Formal Languages and Automata Theory

**Topic:** Beyond Finite Memory – Pushdown Automata for Balanced Parentheses and Palindromes

**Institution:** Jain (Deemed-to-be University)

**Course:** B.Tech – Computer Science and Engineering (Blockchain Technology)

## Author / Team

- Thirisha Sree C
- Kaviselvan K
- B Pragathi

---

**Developed using Python for educational and academic purposes.**
