import hashlib
import json
import datetime as datetime


class Block():
    """docstring for Block."""

    def __init__(self,nonce,tstamp,transaction,p_hash=""):
        self.nonce = nonce
        self.tstamp = tstamp
        self.transaction = transaction
        self.p_hash = p_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string  = json.dumps({"nonce":self.nonce,"tstamp":self.tstamp,"transaction":self.transaction,"p_hash":self.p_hash},sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def __str__(self):
        string = "nonce: "+ str(self.nonce)+"\n"
        string += "tstamp: "+str(self.tstamp)+"\n"
        string += "transaction: "+str(self.transaction)+"\n"
        string += "p_hash: "+str(self.p_hash)+"\n"
        string += "hash: "+str(self.hash)+"\n"

        return string

class BlockChain():
    def __init__(self):

        self.chain = [self.generate_genesis_block(),]

    def generate_genesis_block(self):
        return Block(0,'02/06/1997','genesis_block')

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self,new_block):
        new_block.p_hash = self.get_last_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            p_block = self.chain[i-1]
            curr_block = self.chain[i]
            if(curr_block.hash != curr_block.calculate_hash()):
                print("INVALID BLOCK.....")
                return False
            if(curr_block.p_hash != p_block.hash):
                print("INVALID CHAIN.....")
                return False
        return True

obj = BlockChain()


obj.add_block(Block(0,str(datetime.datetime.now()),99))


for b in obj.chain:
    print("******************************")
    print(b)
    print("******************************")
