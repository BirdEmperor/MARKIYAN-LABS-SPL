# main.py
from Lab7.api.api_client import APIClient
from Lab7.api.repository import DataRepository
from Lab7.core.transaction import Transactions
from Lab7.ui.user_interface import UserInterface
from Lab7.core.error_handler import ErrorHandler

def main():
    try:
        api_client = APIClient("https://jsonplaceholder.typicode.com")
        repository = DataRepository(api_client)
        transactions = Transactions()
        ui = UserInterface(repository, transactions)
        
        ui.start()
        transactions.save_history()
    except Exception as e:
        ErrorHandler.handle_error(e)

if __name__ == "__main__":
    main()
