from appium.options.common.base import AppiumOptions
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

def test_comprar_camiseta():

    options = AppiumOptions()
    options.load_capabilities({

        # Configurações do Appium para o dispositivo físico Android
        "platformName": "Android",
        "appium:platformVersion": "13.0",
        "appium:deviceName": "emulator5554",
        "appium:deviceOrientation": "portrait",
        "appium:appPackage": "com.saucelabs.mydemoapp.android",
        "appium:appActivity": "com.saucelabs.mydemoapp.android.view.activities.SplashActivity",
        "appium:automationName": "UiAutomator2",
        "browserName": "",
        "appium:ensureWebviewsHavePages": True
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    lblSecao = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecao.text == "Products"

    mochilaVermLabel = driver.findElement(AppiumBy.androidUIAutomator("new UiSelector().text(\"Sauce Labs Backpack (red)\")"));
    mochilaVermPrice = driver.findElement(AppiumBy.androidUIAutomator("new UiSelector().resourceId(\"com.saucelabs.mydemoapp.android:id/priceTV\").instance(3)"));
    assert mochilaVermLabel.text == "Sauce Labs Backpack (red)"
    assert mochilaVermPrice.text == "$29.99"
    imgMochilaVerm = driver.findElement(AppiumBy.XPATH, value="(//android.widget.ImageView[@content-desc=\"Product Image\"])[4]")
    imgMochilaVerm.click();

    lblSecaoProduto = driver.findElement(AppiumBy.ACCESSIBILITY_ID, value="title");
    assert lblSecaoProduto.text == "Sauce Labs Backpack (red)"
    lblPrecoProduto = driver.findElement(AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV");
    assert lblPrecoProduto.text == "$29.99"
    sltCor = driver.findElement(AppiumBy.ACCESSIBILITY_ID, value="Red color");
    sltCor.click();
    txtQuantidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/noTV")
    assert txtQuantidade.text == "1"
    btnAddCarrinho = driver.findElement(AppiumBy.ID, value="Tap to add product to cart");
    btnAddCarrinho.click();
    lblQuantidadeNoCarrinho = driver.find_element(by=AppiumBy.ANDROID_UIAUTOMATOR, value="new UiSelector().className(\"android.widget.ImageView\").instance(3)")
    assert lblQuantidadeNoCarrinho.get_attribute("content-desc") == "1"
    lblQuantidadeNoCarrinho.click()

    lblSecaoCarrinho = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecaoCarrinho.text == "Cart"
    lblNomeProdutoCarrinho = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/productTV")
    assert lblNomeProdutoCarrinho.text == "Sauce Labs Backpack (red)"
    lblPrecoProdutoCarrinho = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/priceTV")
    assert lblPrecoProdutoCarrinho.text == "$29.99"
    btnFinalizarCompra = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Confirms products for checkout")
    btnFinalizarCompra.click()

    lblSecaoLogin = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecaoLogin.text == "Login"
    txtUsuario = driver.find_element(by=AppiumBy.ID, value="new UiSelector().resourceId(\"com.saucelabs.mydemoapp.android:id/nameET\")")
    txtUsuario.send_keys("bod@example.com")
    txtSenha = driver.find_element(by=AppiumBy.ID, value="new UiSelector().resourceId(\"com.saucelabs.mydemoapp.android:id/passwordET\")")
    txtSenha.send_keys("10203040")
    btnLogin = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Tap to login")
    btnLogin.click()

    lblSecaoCheckout1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecaoCheckout1.text == "Checkout"
    txtNome = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/fullNameET")
    txtNome.send_keys("David Reynolds")
    txtEndereco = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/address1ET")
    txtEndereco.send_keys("123 Main St, Springfield, USA")
    txtCidade = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/cityET")
    txtCidade.send_keys("Springfield")
    txtEstado = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/stateET")
    txtEstado.send_keys("IL")
    txtCep = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/zipET")
    txtCep.send_keys("62701")
    txtPais = driver.find_element(by=AppiumBy.ID, value="com.saucelabs.mydemoapp.android:id/countryET")
    txtPais.send_keys("USA")        
    btnContinuar = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Saves user info for checkout")
    btnContinuar.click()

    lblSecaoCheckout2 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="title")
    assert lblSecaoCheckout2.text == "Checkout"






    driver.quit()