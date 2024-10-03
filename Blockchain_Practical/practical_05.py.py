from hashlib import sha256
import time

class Block:
    def __init__(self, tirestamp, data, previous_hash):
        self.tirestamp = tirestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        return sha256((str(self.tirestamp) + str(self.data) + str(self.previous_hash)).encode()).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(time.ctime(), "genesisBlock", "00000")

    def mine_block(self, data):
        new_block = Block(time.ctime(), data, self.chain[-1].hash)
        self.chain.append(new_block)

    def print_blockchain(self):
        for i, block in enumerate(self.chain):
            print(f"\nBlock {i}")
            print(f"tirestamp: {block.tirestamp}")
            print(f"data: {block.data}")
            print(f"previousHash: {block.previous_hash}")
            print(f"hash: {block.hash}")

CEVcoin = Blockchain()

data = input("data = ")

print("\nMining New Block -->")
CEVcoin.mine_block(data)

print("\nNew Block mined successfully!")

CEVcoin.print_blockchain()
