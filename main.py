from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import unittest

FIRST_NAME = "Sandra"
SHORT_FIRST_NAME = "Al"
LAST_NAME = "Kot"
SHORT_LAST_NAME = "Po"
EMAIL = "kinoko@wp.pl"
INVALID_EMAIL_NO_DOT = "kot@wppl"
INVALID_EMAIL_NO_AT = "kotwp.pl"
PASSWORD = "Qweasdzxc123"
INCORRECT_PASSWORD = "Qweasdzxc124"
SHORT_PASSWORD = "123"

class SerfentaShop(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://serfenta.pl/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()

    def enterRegistrationForm(self):
        driver = self.driver

        shop_button = self.driver.find_elements(By.CSS_SELECTOR, ".navbar-nav li")[1]
        shop_button.click()

        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "loader")))

        login_link = driver.find_elements(By.CSS_SELECTOR, ".header-menu-element")[0]
        login_link.click()

        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "loader")))

        login_link = driver.find_element(By.CSS_SELECTOR, "main form a")
        login_link.click()

        WebDriverWait(driver, 30).until(EC.invisibility_of_element_located((By.ID, "loader")))

    def testRegistrationFirstNameNotProvided(self):
        self.enterRegistrationForm()
        driver = self.driver

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#billing\[name\]-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationFirstNameNotProvided.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(1, len(errors))

    def testRegistrationFirstNameTooShort(self):
        self.enterRegistrationForm()
        driver = self.driver

        short_first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        short_first_name_input.send_keys(SHORT_FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#billing\[name\]-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationFirstNameTooShort.png")

        self.assertIn(error_text, "Proszę o podanie przynajmniej 3 znaków.")
        self.assertEqual(1, len(errors))

    def testRegistrationLastNameNotProvided(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#billing\[surname\]-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationLastNameNotProvided.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(1, len(errors))

    def testRegistrationLastNameTooShort(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        short_last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        short_last_name_input.send_keys(SHORT_LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#billing\[surname\]-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationLastNameTooShort.png")

        self.assertIn(error_text, "Proszę o podanie przynajmniej 3 znaków.")
        self.assertEqual(1, len(errors))

    def testRegistrationEmailNotProvided(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#email-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationEmailNotProvided.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(1, len(errors))

    def testRegistrationInvalidEmailNoDot(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        invalid_email_no_dot_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        invalid_email_no_dot_input.send_keys(INVALID_EMAIL_NO_DOT)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#email-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationInvalidEmailNoDot.png")

        self.assertIn(error_text, "Proszę o podanie prawidłowego adresu email.")
        self.assertEqual(1, len(errors))

    def testRegistrationInvalidEmailNoAt(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        invalid_email_no_at_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        invalid_email_no_at_input.send_keys(INVALID_EMAIL_NO_AT)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#email-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationInvalidEmailNoAt.png")

        self.assertIn(error_text, "Proszę o podanie prawidłowego adresu email.")
        self.assertEqual(1, len(errors))

    def testRegistrationPasswordNotProvided(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#password-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationPasswordNotProvided.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(2, len(errors))

    def testRegistrationRepeatPasswordNotProvided(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#repassword-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationRepeatPasswordNotProvided.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(1, len(errors))

    def testRegistrationPasswordTooShort(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        short_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        short_password_input.send_keys(SHORT_PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#password-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationPasswordTooShort.png")

        self.assertIn(error_text, "Proszę o podanie przynajmniej 6 znaków.")
        self.assertEqual(2, len(errors))

    def testRegistrationRepeatPasswordTooShort(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        short_repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        short_repeat_password_input.send_keys(SHORT_PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#repassword-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationRepeatPasswordTooShort.png")

        self.assertIn(error_text, "Proszę o podanie przynajmniej 6 znaków.")
        self.assertEqual(1, len(errors))

    def testRegistrationIncorrectRepeatPassword(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(INCORRECT_PASSWORD)

        RODO_checkbox = driver.find_element(By.CSS_SELECTOR, "input[name='rodo']")
        RODO_checkbox.click()

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#repassword-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationIncorrectRepeatPassword.png")

        self.assertIn(error_text, "Proszę o podanie tej samej wartości ponownie.")
        self.assertEqual(1, len(errors))

    def testRegistrationRodoNotAccepted(self):
        self.enterRegistrationForm()
        driver = self.driver

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[name]']")
        first_name_input.send_keys(FIRST_NAME)

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[name='billing[surname]']")
        last_name_input.send_keys(LAST_NAME)

        email_input = driver.find_element(By.CSS_SELECTOR, "input[name='email']")
        email_input.send_keys(EMAIL)

        password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
        password_input.send_keys(PASSWORD)

        repeat_password_input = driver.find_element(By.CSS_SELECTOR, "input[name='repassword']")
        repeat_password_input.send_keys(PASSWORD)

        register_button = driver.find_element(By.CSS_SELECTOR, "main form button[type='submit']")
        register_button.click()

        errors = driver.find_elements(By.CSS_SELECTOR, "label.error")
        error_text = driver.find_element(By.CSS_SELECTOR, "#rodo-error").text

        self.driver.save_screenshot("./screenshots/testRegistrationRodoNotAccepted.png")

        self.assertIn(error_text, "To pole jest wymagane.")
        self.assertEqual(1, len(errors))
