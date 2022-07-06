# Пример 24
import lesson5_2

def print_numbers(limit):
    for i in range(limit):
        print(i)
        
def main():
    lesson5_2.hello()
    print_numbers(3)
    print()
    print_numbers(5)
    
if __name__ == "__main__":
    main()