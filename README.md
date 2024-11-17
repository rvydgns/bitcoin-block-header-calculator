# Bitcoin Block Header Calculator

## Description
This project implements a Python script that calculates the **block hash** and **target string** for a given Bitcoin block header. It follows the Bitcoin protocol specifications for block header construction, SHA-256 double hashing, and target calculation based on the "bits" field.

### Key Features
- Converts block header fields (e.g., version, previous block hash, Merkle root, timestamp) to the proper format.
- Computes the block hash using the **SHA-256 double-hash** algorithm.
- Calculates the mining difficulty target based on the "bits" value.
- Allows testing with different `nonce` values to simulate mining.

## Input Fields
The script requires the following inputs:
- **Version**: Version of the block (e.g., `0x20000000`).
- **Previous Block Hash**: Hash of the previous block in the chain.
- **Merkle Root**: Root hash of all transactions in the block.
- **Datetime**: The block's creation time in the format `YYYY-MM-DD HH:MM:SS GMT+1`.
- **Bits**: Encoded representation of the difficulty target.
- **Nonce**: A 32-bit number used in mining to vary the block hash.

## Output
The script calculates and prints:
1. **BlockHash**: The final SHA-256 double-hashed value of the block header.
2. **TargetStr**: The calculated difficulty target as a 64-character hexadecimal string.
3. **BlockHash with Random Nonce**: The block hash calculated with a different nonce value for testing.
