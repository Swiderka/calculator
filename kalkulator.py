
import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def kalkulator (a, b, wybor):
    if wybor == "1":
        logging.info(f"Dodaje {a} i {b}.")
        return a + b
    elif wybor == "2":
        logging.info(f"Odejmuje {b} od {a}.")
        return a - b
    elif wybor == "3":
        logging.info(f"Mnoze {a} i {b}.")
        return a / b
    elif wybor == "4":
        logging.info(f"Dziele {a} przez {b}.")
    else:
        exit(1)



if __name__ == "__main__":
    wybor = input("Podaj dzialanie, poslugujac sie odpowiednia liczba: 1 Dodawanie, 2 Odejmowanie, 3 Mnozenie, 4 Dzielenie:")
    a = float(input("Podaj skladnik 1."))
    b = float(input("Podaj skladnik 2."))
   
    print(f"Wynik to {kalkulator (a, b, wybor)}")
