import hashlib
import time

class Block:
    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no, self.prev_hash, self.data, self.timestamp)
        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def formatted_output(self):
        return "{}-{}-{}-{}-{}]".format(self.index, self.proof_no, self.prev_hash, len(self.data), self.timestamp)

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash="0")

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data,
        )
        self.current_data = []
        self.chain.append(block)
        return block

    def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1
        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):
        self.new_data(sender="Sipna COET", recipient=details_miner, quantity=1)
        last_block = self.latest_block
        proof_no = self.proof_of_work(last_block.proof_no)
        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)
        return block

blockchain = BlockChain()

print("**Mining feeCoin about to start**\n")

genesis_block = blockchain.chain[0]
print(f"{genesis_block.formatted_output()}\n")

last_block = blockchain.latest_block
proof_no = blockchain.proof_of_work(last_block.proof_no)

blockchain.new_data(
    sender="Sipna COET",
    recipient="SIPNA CSE Department",
    quantity=1
)

new_block = blockchain.block_mining(details_miner="SIPNA CSE Department")

print("**Mining feeCoin has been successful**\n")

print(f"{new_block.index} {new_block.proof_no} {new_block.prev_hash} {new_block.timestamp}. 1\n")
print(f"{proof_no}\n")
print(f"{new_block.calculate_hash} [{{'sender': 'Sipna COET', 'recipient': 'SIPNA CSE Department', 'quantity': 1}}]-{new_block.timestamp}\n")
