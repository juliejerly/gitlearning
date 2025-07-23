from pages.base_page import BasePage


class HomePage(BasePage):

    add_to_cart = ".btn_inventory"
    shopping_cart_link = ".shopping_cart_link"
    inventory_item_name = ".inventory_item_name"

    def verify_page(self, selector, expected):
        self.verify_current_page(selector, expected)

    def get_first_item_name(self):
        return self.get_text(self.inventory_item_name)

    def click_add_to_cart(self):
        self.click(self.add_to_cart)

    def click_shopping_cart_link(self):
        self.click(self.shopping_cart_link)








