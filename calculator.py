# !/Users/akorol/Desktop/University/Software_testing/Labs/lab2/env/bin/python3
import sys
import time
from PIL import Image
from io import BytesIO
from selenium import webdriver
import platform
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QImage, QPalette, QBrush, QIcon, QColor, QPixmap
from PyQt5.QtWidgets import *
from colour import Color
from PyQt5.QtCore import Qt
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains

# https://stackoverflow.com/questions/15018372/how-to-take-partial-screenshot-with-selenium-webdriver-in-python
class MainWindow(QMainWindow):
    DARWIN_EXEC = "./chromdriver"
    WINDOWS_EXEC = ".\chromdriver.exe"
    LINUX_EXEC = "chromdriver_linux"
    def __init__(self):
        QMainWindow.__init__(self)
        self.driver = None
        self.ui = uic.loadUi('calc.ui')

        self.result = None

        self.setAutoFillBackground(True)
        p = QPalette()
        p.setColor(self.backgroundRole(), QColor(192, 192, 192))
        self.ui.setPalette(p)

        # инконка приложения
        self.ui.setWindowIcon(QIcon('icon.png'))

        # кнопки
        self.ui.sin_button.setToolTip('sin(x)')
        self.ui.sin_button.setCheckable(True)
        self.ui.sin_button.setAutoExclusive(True)
        self.ui.sin_button.toggled.connect(self.sinx)

        self.ui.cos_button.setToolTip('cos(x)')
        self.ui.cos_button.setCheckable(True)
        self.ui.cos_button.setAutoExclusive(True)
        self.ui.cos_button.toggled.connect(self.cosx)

        self.ui.tg_button.setToolTip('tg(x)')
        self.ui.tg_button.setCheckable(True)
        self.ui.tg_button.setAutoExclusive(True)
        self.ui.tg_button.toggled.connect(self.tgx)

        self.ui.ctg_button.setToolTip('ctg(x)')
        self.ui.ctg_button.setCheckable(True)
        self.ui.ctg_button.setAutoExclusive(True)
        self.ui.ctg_button.toggled.connect(self.ctgx)


        self.ui.expr_button.setToolTip('expr()')
        self.ui.expr_button.setCheckable(True)
        self.ui.expr_button.setAutoExclusive(True)
        self.ui.expr_button.toggled.connect(self.expr)

        self.ui.null_button.setToolTip('Clean lineEdit')
        self.ui.null_button.pressed.connect(self.null)

        self.ui.count_button.setToolTip('Count')
        self.ui.count_button.pressed.connect(self.count)

        self.ui.lineEdit.textChanged.connect(self.update_result)
        self.ui.show()

    def error_message(self):
        QMessageBox.about(self, 'Error', 'Invalid number')

    def show_answer(self):
        box = QMessageBox()
        box.setWindowTitle("Wassap slappers")
        box.setText("Answer")
        box.setIconPixmap(QPixmap("res.png"))
        box.exec_()

    def set_uncheckable(self, button):
        buttons_list = [self.ui.sin_button,
                        self.ui.cos_button,
                        self.ui.tg_button,
                        self.ui.ctg_button]

        for i in range(len(buttons_list)):
            if buttons_list[i] != button:
                buttons_list[i].setChecked(False)

    def expr(self):
        self.result = self.ui.lineEdit.text()

    def update_result(self):
        self.result = self.ui.lineEdit.text()

    def sinx(self):
        try:
            self.set_uncheckable(self.ui.sin_button)
            x = self.ui.lineEdit.text()
            num = str(math.sin(int(x)))
            self.result = num
        except (ValueError, ZeroDivisionError) as e:
            print(f'Error: {e}')
            self.error_message()

    def cosx(self):
        try:
            self.set_uncheckable(self.ui.cos_button)
            x = self.ui.lineEdit.text()
            num = str(math.cos(int(x)))
            self.result = num
        except (ValueError, ZeroDivisionError) as e:
            print(f'Error: {e}')
            self.error_message()

    def tgx(self):
        try:
            self.set_uncheckable(self.ui.tg_button)
            x = self.ui.lineEdit.text()
            num = str(math.tan(int(x)))
            self.result = num
        except (ValueError, ZeroDivisionError) as e:
            print(f'Error: {e}')
            self.error_message()

    def ctgx(self):
        try:
            self.set_uncheckable(self.ui.ctg_button)
            x = self.ui.lineEdit.text()
            num = str(math.cos(int(x)) / math.sin(int(x)))
            self.result = num
        except (ValueError, ZeroDivisionError) as e:
            print(f'Error: {e}')
            self.error_message()
    

    def _(self):
        option = webdriver.ChromeOptions()
        os_name = platform.system()
        option.add_argument("--incognito")
        print(os_name)
        if os_name == "Darwin":
            self.driver = webdriver.Chrome(chrome_options=option)
        elif os_name == "Windows":
            self.driver = webdriver.Chrome(executable_path=type(self).WINDOWS_EXEC, chrome_options=option)
        elif os_name == "Linux":
            self.driver = webdriver.Chrome(executable_path=type(self).LINUX_EXEC, chrome_options=option)
        while 1:
            try:
                self.driver.get("https://www.symbolab.com/solver/trigonometric-simplification-calculator")
                el = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main-input"]/span/textarea')))
                break
            except TimeoutException:
                pass
        el.clear()
        dig = 0
        for i in self.result:
            if dig:
                if i.isdigit() == False:
                    el.send_keys(u'\ue014')
                    dig = 0
            el.send_keys(i)
            if i == "^":
                dig = 1
        self.driver.find_element(By.XPATH, '//*[@id="Codepad"]/div[4]/button').click()

        # gets visible method
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="steps-container"]/li[2]/div[1]')))
        except TimeoutException:
            self.error_message()

        # Div with answer
        last_el = self.driver.find_elements(By.XPATH, "//li[@class='solution_step_list_item']")[-1]
        element = last_el.find_element(By.XPATH, ".//div[@class='solution_step_result']")
        ActionChains(self.driver).move_to_element(element).perform()
        loc = element.location
        size = element.size
        x = math.floor(loc["x"])
        y = math.floor(loc["y"])
        w = math.ceil(size["width"])
        h = math.ceil(size["height"])

        # Central Div
        add = self.driver.find_element(By.XPATH, '//*[@id="solution_page"]/div[7]/div[1]/div')
        addh = add.size['height']
        addw = add.size['width']
        
        # Right ad
        right_add = self.driver.find_element(By.XPATH, '//*[@id="solution_page"]/div[7]/div[3]')
        raddh = right_add.size['height']
        raddw = right_add.size['width']

        png = self.driver.get_screenshot_as_png()
        self.driver.quit()
        im = Image.open(BytesIO(png))   
        width, height = im.size
        a = im.crop((x+addw+50, height-(h+h//2 + 8), width-(w+x+addw+raddw), height))
        a.save("res.png")
        self.show_answer()

    def null(self):
        self.ui.lineEdit.setText("")
        self.result = ''

    def count(self):
        if self.ui.expr_button.isChecked():
            self._()
        else:
            self.msg = QMessageBox()
            self.msg.setStyleSheet('background-color: #d3d3d3')
            self.msg.setWindowIcon(QIcon('icon.png'))
            self.msg.setWindowTitle("Result")
            if not self.result:
                self.msg.setText("Nothing to compute")
            else:
                self.msg.setText(self.result)
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.exec_()
            if not self.ui.sin_button.isChecked():
                self.ui.sin_button.setChecked(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
