# RSA decryption
Simple Python scripts to help you to decrypt RSA-encrypted data. The repository provides multiple Python scripts which target different weaknesses in RSA encryption. The repository also provides RSA challenges to practise on.
# Attacks:
1. rsa_decrypt_with_n_p_q_e.py
  A simple Python script which will decrypt RSA data if you know n, p, q and e values.
  To find p and q values you can try visiting http://www.factordb.com/ and entering n. If n is small you can attempt a brute force attack to find p and q values.
2. find_p_q.py
   A simple Python script to find p and q values up to around 100,000,000 (depending on the computing power)
3. rsa_bruteforce_small_e.py
   A simple Python script which will bruteforce RSA for small e values and m^e is barely larger than n.
# Helpful resources:
1. https://ctf101.org/cryptography/what-is-rsa/
2. https://www.youtube.com/watch?v=4zahvcJ9glg&ab_channel=EddieWoo, https://www.youtube.com/watch?v=oOcTVTpUsPQ&ab_channel=EddieWoo
3. http://www.factordb.com/ will help to exploit Weak public key factorization
# Practise:
1. The repository will provide a Python script for solving problems, containing problems for practising with different RSA vulnerability scenarios.
2. https://picoctf.org/
