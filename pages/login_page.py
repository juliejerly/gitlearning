from pages.base_page import BasePage

class LoginPage(BasePage):
    signup = ".fa-lock"
    user_name = "#user-name"
    user_password = "#password"
    login_btn="#login-button"

    def enter_credentials(self, url, username,password):
        self.navigate(url)
        self.click(self.user_name)
        self.fill(self.user_name, username)
        self.click(self.user_password)
        self.fill(self.user_password, password)
        self.click(self.login_btn)




