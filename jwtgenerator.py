# Python 3.x
import secrets

# Generate a 32-byte (256-bit) secure random key
jwt_secret = secrets.token_hex(32)
print("Your new JWT_SECRET_KEY:", jwt_secret)
