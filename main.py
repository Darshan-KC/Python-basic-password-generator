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
    def generate(self):
        password = []
        for i in range(self.length):
            char_type = self.get_pseudo_random(1, 4)  # 1: Uppercase, 2: Lowercase, 3: Number, 4: Symbol
            if char_type == 1:
                password.append(chr(self.get_pseudo_random(65, 90)))  # Uppercase
            elif char_type == 2:
                password.append(chr(self.get_pseudo_random(97, 122)))  # Lowercase
            elif char_type == 3:
                password.append(chr(self.get_pseudo_random(48, 57)))   # Numbers
            else:
                # Symbols like !, #, $, %, &, @ (ASCII 33 to 38, 64)
                symbols = [33, 35, 36, 37, 38, 64]
                symbol_index = self.get_pseudo_random(0, len(symbols) - 1)
                password.append(chr(symbols[symbol_index]))
        return ''.join(password)

def main():
    length = 8
    generate = SimplePassword(length)
    password = generate.generate()
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()