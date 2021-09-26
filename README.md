# RSA-signature
One digital signature scheme (of many) is based on RSA. To create signature keys, generate an RSA key pair containing a modulus, N, that is the product of two random secret distinct large primes, along with integers, e and d, such that e d ≡ 1 (mod φ(N)), where φ is the Euler's totient function. The signer's public key consists of N and e, and the signer's secret key contains d.  

To sign a message, m, the signer computes a signature, σ, such that σ ≡  md (mod N). To verify, the receiver checks that σe ≡ m (mod N).
