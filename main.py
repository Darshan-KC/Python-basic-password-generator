class PasswordGenerator:
    def __init__(self, length:int) -> None:
        self.length = length
        self.seed = 1234567
        self.seed = self._generate_initial_seed()
    
    def _generate_initial_seed(self):
        """
        Generate a dynamic initial seed based on multiple changing factors.
        
        Returns:
            int: A dynamically generated seed value
        """
        # Combine multiple sources of "randomness" without external modules
        factor1 = 12345  # Constant factor
        factor2 = 54321  # Another constant factor
        
        # Use object's memory address and its changing state as a source of variation
        factor3 = id(self)
        
        # Create a seed that changes between runs
        return (factor1 * factor2 + factor3) % (2**32)
        
    def generate(self):
        """Base method to be overridden in subclasses."""
        raise NotImplementedError("Sub classes must implemented this method")

    def get_pseudo_random(self,min_val, max_val):
        """
        Generate a pseudo-random number using mathematical operations.
        
        Args:
            min_val (int): Minimum value of the range
            max_val (int): Maximum value of the range
        
        Returns:
            int: A pseudo-randomly generated number within the specified range
        """
        
        # Linear Congruential Generator (LCG) algorithm
        # LCG parameters chosen to provide good distribution
        a = 1664525   # Multiplier
        c = 1013904223  # Increment
        m = 2**32     # Modulus
        
        # Update seed using LCG formula
        self.seed = (a * self.seed + c) % m
        
        # Scale the random value to the desired range
        random_value = min_val + (self.seed % (max_val - min_val + 1))
        
        return random_value
        
    
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

class StrongPassword(PasswordGenerator):
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
    # length = 8
    # generate = SimplePassword(length)
    # password = generate.generate()
    # print(f"Generated Password: {password}")
    try:
        strength = input("Select password strength (simple, intermediate, strong): ").strip().lower()
        length = int(input("Enter the length of the password: "))

        if strength == "simple":
            generator = SimplePassword(length)
        elif strength == "intermediate":
            generator = IntermediatePassword(length)
        elif strength == "strong":
            generator = StrongPassword(length)
        else:
            print("Invalid strength selected.")
            return

        password = generator.generate()
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Length should be an integer.")

if __name__ == "__main__":
    main()