import os, time
from rich.console import Console

console = Console()

os.system("cls||clear")

def formatNumber(num):
    return int(num) if num % 1 == 0 else num

def is_float(element: any) -> bool:
    if element is None: 
        return False
    
    try:
        float(element)
        return True
    except ValueError:
        return False

def calculate(num1, num2, operation) -> str:
    num1 = formatNumber(float(num1))
    num2 = formatNumber(float(num2))

    if operation == "+":
        return str(num1 + num2)
    elif operation == "-":
        return str(num1 - num2)
    elif operation == "*":
        return str(num1 * num2)
    elif operation == "/":
        if num2 == 0:
            return "divbyzero"
        return str(formatNumber(num1 / num2))
    else:
        return "invalid"

while True:
    console.print("Welcome to Calculator!", end="\n\n", style="bold underline green")

    console.print("Please enter the first number: ", style="bold blue")
    num1 = input().strip()

    if not is_float(num1):
        os.system("cls||clear")
        console.print("Invalid input. Please enter a valid number.", end="\n\n", style="bold red")
        continue

    console.print()

    console.print("Please enter the second number: ", style = "bold blue")
    num2 = input().strip()

    if not is_float(num2):
        os.system("cls||clear")
        console.print("Invalid input. Please enter a valid number.", end="\n\n", style="bold red")
        continue

    console.print()

    console.print("Please enter the operation [green](+, -, *, /)[/green]: ", end="", style="bold blue")
    operation = input().strip()
    
    result = None

    if operation in ["+", "-", "*", "/"]:
        result = calculate(num1, num2, operation)
    else:
        os.system("cls||clear")
        console.print("Invalid operation. Please enter a valid operation.", end="\n\n", style="bold red")
        continue
    
    console.print()

    if result == "invalid" or result == "divbyzero":
        console.print("Invalid operation." if result == "invalid" else "Invalid operation: cannot divide by zero.", end="\n\n", style="bold red")
    else:
        console.print(f"[bold green]Result is:[/bold green]\n{result}", end="\n\n")

    time.sleep(1)
    console.print("Would you like to try again? (yes/no): ", end="", style="bold blue")

    play_again = input().strip().lower()

    if play_again == "yes":
        os.system("cls||clear")
    else:
        break

    continue
