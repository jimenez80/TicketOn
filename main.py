from src.core.app import start_system

def main():
    print("=" * 40)
    print("      Bienvenido a TicketOn")
    print("=" * 40)

    result = start_system()
    print(result)

if __name__ == "__main__":
    main()