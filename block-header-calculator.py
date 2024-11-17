import hashlib
import time

def calculate_blockhash(version, previousblockhash, merkleroot, datetime, bits, nonce):
    def to_little_endian(value):
        return bytes.fromhex(value)[::-1].hex()

    version_le = to_little_endian(version[2:])
    previousblockhash_le = to_little_endian(previousblockhash)
    merkleroot_le = to_little_endian(merkleroot)
    timestamp = int(time.mktime(time.strptime(datetime, "%Y-%m-%d %H:%M:%S GMT+1")))
    timestamp_le = to_little_endian(f"{timestamp:08x}")

    header_hex = (
        version_le +
        previousblockhash_le +
        merkleroot_le +
        timestamp_le +
        bits[2:] +
        nonce[2:]
    )
    header_bin = bytes.fromhex(header_hex)
    blockhash = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()[::-1].hex()
    return blockhash

def calculate_target(bits):
    exponent = int(bits[2:4], 16)
    coefficient = int(bits[4:], 16)
    return f"{coefficient * (2 ** (8 * (exponent - 3))):064x}"

version = "0x20000000"
previousblockhash = "000000000000000000080bee5a07348e1a97b0a5f024beb7eb2b24d3c2de3021"
merkleroot = "d519612f62ae09e7df4c233d9f63d04f65869b4dbbf7833c4bda518df5d2c4c5"
datetime = "2024-11-15 10:25:43 GMT+1"
bits = "0x170dd543"
nonce = "0x2a9f2aa4"

blockhash = calculate_blockhash(version, previousblockhash, merkleroot, datetime, bits, nonce)
target_str = calculate_target(bits)
nonce_random = "0x12345678"
blockhash_random = calculate_blockhash(version, previousblockhash, merkleroot, datetime, bits, nonce_random)

print("BlockHash:", blockhash)
print("TargetStr:", target_str)
print("Random Nonce BlockHash:", blockhash_random)
