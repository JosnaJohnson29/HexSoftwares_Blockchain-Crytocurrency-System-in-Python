import hashlib

class NeuralcoinBlock:

    def  __init__(self,previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list

        self.block_data = "-".join(self.transaction_list) + "-" + self.previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = "Anna Sends 2 NC to Mike"   
t2 = "Bob Sends 4.1 NC to Mike" 
t3 = "Mike Sends 3.2 NC to Bob" 
t4 = "Daniel Sends 0.3 NC to Anna" 
t5 = "Mike Sends 1 NC to Charlie" 
t6 = "Mike Sends 5.4 NC to Daniel"      

initial_block = NeuralcoinBlock("Initial String" ,[t1 , t2])

print(initial_block.block_data)
print(initial_block.block_hash)

second_block = NeuralcoinBlock(initial_block.block_hash ,[t3 , t4])

print(second_block.block_data)
print(second_block.block_hash)

third_block = NeuralcoinBlock(second_block.block_hash ,[t5 , t6])

print(third_block.block_data)
print(third_block.block_hash)   
