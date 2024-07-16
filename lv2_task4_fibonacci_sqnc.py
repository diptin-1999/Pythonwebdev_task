def generate_fibonacci_sequence(terms):
    fibonacci_sequence = []
    a, b = 0, 1
    for _ in range(terms):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    return fibonacci_sequence

def main():
    try:
        num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
            return
        fibonacci_sequence = generate_fibonacci_sequence(num_terms)
        print("Fibonacci sequence up to", num_terms, "terms:")
        print(fibonacci_sequence)
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    main()
