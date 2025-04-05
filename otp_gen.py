import random

def generate_otp(length):
    otp = ''.join(str(random.randint(0, 9))
for _ in range(length))
    return otp
print(generate_otp(4))