import sys, os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))  # Добавляем родительский каталог

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC



class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 20)

    def get_current_url(self):
        return self.driver.current_url

    def find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located(locator)
            )
            return element
        except TimeoutException:
            raise


    def wait_until_element_visibility(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))


    def click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator)
            )
            element.click()
        except NoSuchElementException:
            raise

    def send_keys_to_element(self, locator, order_data, timeout: int = 10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            element.send_keys(order_data)
        except NoSuchElementException:
            raise


    def get_element_text(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
            if element:
                return element.text
        except NoSuchElementException:
            raise

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def check_url(self, expected_url, timeout: int = 10):
        try:
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))
            return True  # URL соответствует ожидаемому
        except TimeoutException:
            return False  # URL не соответствует ожидаемому


    def check_invisibility(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))


    def drag_and_drop_element(self, source_element, target_element):
        script = """
        function simulateHTML5DragAndDrop(sourceNode, destinationNode) {
            var dataTransfer = new DataTransfer();
            var dragStartEvent = new DragEvent('dragstart', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragStartEvent);

            var dropEvent = new DragEvent('drop', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            destinationNode.dispatchEvent(dropEvent);

            var dragEndEvent = new DragEvent('dragend', {
                bubbles: true,
                cancelable: true,
                dataTransfer: dataTransfer
            });
            sourceNode.dispatchEvent(dragEndEvent);
        }
        simulateHTML5DragAndDrop(arguments[0], arguments[1]);
        """
        source_element = self.driver.find_element(*source_element)
        target_element = self.driver.find_element(*target_element)
        self.driver.execute_script(script, source_element, target_element)

    def wait_until_element_closed(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    def find_until_all_elements_located(self, *locator):
        return WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(*locator))

    def wait_url_to_be(self, url):
        WebDriverWait(self.driver, 30).until((EC.url_to_be(url)))

    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        self.find_element(locator)











