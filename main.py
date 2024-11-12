class PasswordGenerator:
    def __init__(self, length:int) -> None:
        self.length = length
        
    def generate(self):
        """Base method to be overridden in subclasses."""
        raise NotImplementedError("Sub classes must implemented this method")

    def get_pseudo_random(self,min_val, max_val):
        pass
    
class SimplePassword(PasswordGenerator):
    pass

class IntermediatePassword(PasswordGenerator):
    pass

class strongPassword(PasswordGenerator):
    pass

def main():
    pass

if __name__ == "__main__":
    main()