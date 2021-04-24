load_file_in_context('blockchain.py')
load_file_in_context('blockchain_test.py')

test_block = Block(1,0)

test_blockchain = Blockchain_test()
real_blockchain = Blockchain()

test_proof = test_blockchain.proof_of_work(test_block)
real_proof = real_blockchain.proof_of_work(test_block)

if test_proof == real_proof:
  pass_tests()
else:
  fail_tests()
