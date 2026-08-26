# 🔗 Neuralcoin – Simple Blockchain in Python

A simple educational **Blockchain/Cryptocurrency system** developed using Python.

This project demonstrates the basic concept of how blockchain blocks can contain transaction information and how blocks can be connected using cryptographic hashes.

## 📌 Project Overview

In this project, I created a `NeuralcoinBlock` class that stores:

* Previous block hash
* Transaction list
* Block data
* SHA-256 block hash

The block hash is generated using Python's `hashlib` library and SHA-256 hashing.

## ⚙️ How It Works

The project creates three blocks.

### Block 1

The first block contains two sample transactions and an initial string:

```text
Anna Sends 2 NC to Mike
Bob Sends 4.1 NC to Mike
```

### Block 2

The second block contains two more transactions and uses the hash of the first block as its previous block hash.

```text
Mike Sends 3.2 NC to Bob
Daniel Sends 0.3 NC to Anna
```

### Block 3

The third block uses the hash of the second block:

```text
Mike Sends 1 NC to Charlie
Mike Sends 5.4 NC to Daniel
```

These transactions and blocks are defined in the Python program.

## 🧩 Project Structure

```text
Neuralcoin/
│
├── main.py
│
└── README.md
```

## 🛠️ Technologies Used

* Python
* `hashlib`
* SHA-256 Hashing
* Object-Oriented Programming
* Classes and Objects
* Strings
* Lists

## 💻 Code Explanation

The `NeuralcoinBlock` class receives the previous block hash and transaction list:

```python
class NeuralcoinBlock:

    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
```

The transaction data and previous hash are combined to create the block data, and SHA-256 is used to generate the block hash.

## 🔗 Connecting the Blocks

The blocks are connected in sequence:

```text
Initial String
      ↓
  Block 1
      ↓
Block 1 Hash
      ↓
  Block 2
      ↓
Block 2 Hash
      ↓
  Block 3
```

The second block receives the first block's hash, and the third block receives the second block's hash.

## ▶️ How to Run

Make sure Python is installed on your computer.

Open the project folder in **VS Code** or a terminal.

Run:

```bash
python main.py
```

## 📤 Output

The program displays:

* Block data
* Block hash
* Transaction information

Each block produces a SHA-256 hash based on its block data and previous block hash.

## 📚 What I Learned

Through this project, I learned:

* Basic blockchain concepts
* How blocks store transaction data
* How blocks are connected
* SHA-256 hashing
* Python classes and objects
* Using the `hashlib` module
* Creating and working with block data

## 🚀 Future Improvements

This project can be improved by adding:

* Multiple users and wallets
* Transaction validation
* Mining functionality
* Proof of Work
* Blockchain verification
* A graphical user interface
* Persistent blockchain storage

LinkedIn URL:https://www.linkedin.com/posts/josna-johnson-894a29392_python-pythonproject-blockchain-activity-7498331926043324416-vKzY?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGCdu7AB3McqJazzcJ3w2cmEvw-1JU5jJNc
