from src.core.app import start_system

def main():
    print("=" * 40)
    print("      Bienvenido a TicketOn")
    print("=" * 40)

    estado_sistema = start_system()
    print(estado_sistema)

if __name__ == "__main__":
    main()