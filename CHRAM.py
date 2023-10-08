class RAM:
    def __init__(self):
        self.memory = {}  # Dictionary to represent the RAM

    def read(self, address):
        if address in self.memory:
            return self.memory[address]
        else:
            print(f"Error: Address {address} not found in RAM.")
            return None

    def write(self, address, data):
        if 0 <= address <= (2 ** 32 - 1):  # Checking if the address is within the 32-bit range
            self.memory[address] = data
        else:
            print(f"Error: Invalid address {address}. Address must be within 0 and {2 ** 32 - 1}.")

# Example usage:
if __name__ == "__main__":
    ram = RAM()

    # Writing data to RAM at address 0x1000
    ram.write(0x1000, 42)

    # Reading data from RAM at address 0x1000
    data = ram.read(0x1000)
    print("Data at address 0x1000:", data)
