class PasswordGenerator:
    def __init__(self, length:int) -> None:
        self.length = length
        
    def generate(self):
        """Base method to be overridden in subclasses."""
        raise NotImplementedError("Sub classes must implemented this method")

    def get_pseudo_random(self,min_val, max_val):
        """Generate a pseudo-random number using simple math operations."""
        seed = (min_val * 31 + max_val * 17) % 97  # Simple seed calculation
        return (seed * 37 + self.length * 23) % (max_val - min_val + 1) + min_val
    
class SimplePassword(PasswordGenerator):
    def generate(self):
        password = [chr(self.get_pseudo_random(97, 122)) for _ in range(self.length)]
        return ''.join(password)

class IntermediatePassword(PasswordGenerator):
    def generate(self):
        password = []
        for i in range(self.length):
            char_choice = self.get_pseudo_random(0, 1)  # 0 for lowercase, 1 for uppercase
            if char_choice == 0:
                password.append(chr(self.get_pseudo_random(97, 122)))  # Lowercase
            else:
                password.append(chr(self.get_pseudo_random(65, 90)))   # Uppercase
        return ''.join(password)

class strongPassword(PasswordGenerator):
    pass

def main():
    length = 8
    generate = SimplePassword(length)
    password = generate.generate()
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()