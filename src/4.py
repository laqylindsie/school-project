def get_random_code(length=10):
    # Get a list of all possible characters
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    
    # Generate a random string of the specified length
    return ''.join(random.choice(chars) for _ in range(length))
