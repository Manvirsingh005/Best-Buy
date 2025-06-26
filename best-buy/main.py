from products import Product
from store import Store


def list_products(store: Store) -> None:
    print("\nAvailable Products:")
    for product in store.get_all_products():
        print(product.show())
    print("\n")


def show_total_amount(store: Store) -> None:
    total_quantity = store.get_total_quantity()
    print(f"Total items in store: {total_quantity}\n")


def make_order(store: Store) -> None:
    list_products(store)

    shopping_list = []
    while True:
        product_name = input(
            "Enter product name to add to order (or 'done' to finish): "
        ).strip()
        if product_name.lower() == "done":
            break

        quantity_str = input(f"Enter quantity for {product_name}: ")
        if not quantity_str.isdigit():
            print("Please enter a valid number for quantity!")
            continue

        quantity = int(quantity_str)
        product = next(
            (p for p in store.get_all_products() if p.name == product_name), None
        )

        if not product:
            print(f"{product_name} not found!")
        else:
            shopping_list.append((product, quantity))

    if shopping_list:
        try:
            total_cost = store.order(shopping_list)
            print(f"Total order cost: ${total_cost}\n")
        except ValueError as e:
            print(f"Error during order: {e}\n")


def start(store: Store) -> None:
    while True:
        print(
            "1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit\n"
        )
        choice = input("Your choice: ").strip()

        if choice == "1":
            list_products(store)
        elif choice == "2":
            show_total_amount(store)
        elif choice == "3":
            make_order(store)
        elif choice == "4":
            print("Exiting the store. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


def main() -> None:
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
