# Write your imports here
from .item import Bill, Product
from .entity import Buyer



class OrderType:
    # Do not change this enum
    ASC = 0
    DES = 1


class Statistics:
    def __init__(self, bills: list[Bill]):
        # Do not change this method
        self.bills = bills

    def find_top_sell_product(self) -> (Product, int):
        products_sells = {}
        for bill in self.bills:
            for product in bill.products:
                products_sells[product] = products_sells.get(product, 0) + 1
        result = sorted(products_sells.items(), key=lambda x:x[1], reverse=True)

        return result[0]

    def find_top_two_sellers(self) -> list:
        sellers = {}
        for bill in self.bills:
            sellers[bill.seller] = sellers.get(bill.seller, 0) + bill.calculate_total()
        result = sorted(sellers.items(), key=lambda x:x[1], reverse=True)

        return [seller[0] for seller in result[:2]]
    
    def find_buyer_lowest_total_purchases(self) -> (Buyer, float):
        buyers = {}
        for bill in self.bills:
            buyers[bill.buyer] = buyers.get(bill.buyer, 0) + bill.calculate_total()
        result = sorted(buyers.items(), key=lambda x:x[1])

        return result[0]

    def order_products_by_tax(self, order_type: OrderType) -> tuple:
        # Write here your code
        pass

    def show(self):
        # Do not change this method
        print("Bills")
        for bill in self.bills:
            bill.print()
