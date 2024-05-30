import hashlib
import json
from time import time

chain = []

def block(proof, previous_hash = None) :
	transaction = {
	    'sender' : 'Satoshi',
	    'receipent' : 'Mike',
	    'amount' : '5 ETH'
	}
	data = {
	    'index' : 1,
	    'timestamp' : time(),
	    'transaction' : transaction,
	    'gas/fee' : 0.1,
	    'proof' : proof,
	    'previous_hash' : previous_hash,
	}
	chain.append(block)
	print("block infromation: ", data)
	string_object = json.dumps(data)
	block_string = string_object.encode()

	raw_hash = hashlib.sha256(block_string)
	hex_hash = raw_hash.hexdigest()
	print("Hash code of block: ", hex_hash)

block(previous_hash = "No previous hash. Since thsi is the first block.", proof = 000)