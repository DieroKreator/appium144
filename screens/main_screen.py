from appium.webdriver.common.appiumby import AppiumBy
from screens.base_screen import BaseScreen

class MainScreen(BaseScreen):
    titulo_secao = (AppiumBy.ACCESSIBILITY_ID, "title")
    
    def verificar_titulo_secao(self):
        return self.get_text(*self.titulo_secao)
    
    def escolher_produto(self, id_produto):
        self.click_element(AppiumBy.XPATH, f"(//android.widget.ImageView[@content-desc='Product Image'])[{id_produto}]")
        
