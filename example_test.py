def test_dynamicID(page):
    page.goto('/')
    page.click('text = Dynamic ID')
    page.click('text = Button with Dynamic ID')
    text = page.inner_text('h3') 
    assert text == 'Dynamic ID'
    
def test_class_attribute(page):
    page.goto('/')
    page.click('text = Class Attribute')
    page.click("//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    
def test_hidden_layers(page):
    page.goto("/")
    page.click('text = Hidden Layers')
    page.click('#greenButton')
    assert page.is_visible('#blueButton')
    
def test_load_delay(page):
    page.goto("/")
    page.click('text = Load Delay')
    page.click('//*[@class="btn btn-primary"]')
  
def test_ajax_data(page):
    page.goto("/")
    page.click('text = AJAX Data')
    page.click('#ajaxButton')
    page.click('text=Data loaded with AJAX get request')
    assert page.is_visible('text=Data loaded with AJAX get request')

def test_client_side_delay(page):
    page.goto('/')
    page.click('text = Client Side Delay')
    page.click('#ajaxButton')
    page.click('//*[@class="bg-success"]')
    assert page.is_visible('text = Data calculated on the client side.')
    
def test_click(page):
    page.goto('/')
    page.click('text = Click')
    page.click('#badButton')
    badButton = page.is_enabled('#badButton')
    assert badButton

# def test_input(page):
#     page.goto('/')
#     page.click('text = Text Input')
#     page.fill('#newButtonName', "test")
#     page.click("text=Button That Should Change it's Name Based on Input Value")
#     assert page.inner_text('#updatingButton') == "test"

def test_scrollbars(page):
    page.goto("/scrollbars")
    page.click("#hidingButton")
    
def test_dynamic_table(page):
    page.goto("/dynamictable")
    chromeCPU = page.is_visible('//*[@class="bg-warning"]')
    
def test_verify_text(page):
    page.goto("/verifytext")
    assert page.inner_text("//span[normalize-space(.)='Welcome UserName!']") == "Welcome UserName!"
    
def test_progress_bar(page):                   
    page.goto("/progressbar")
    page.click('#startButton')
    page.inner_text('#progressBar[aria-valuenow="75"]')
    page.click('#stopButton')
    page.wait_for_timeout(4000)
    assert  "Result: 0" in page.inner_text('#result')
       
# def test_visibility(page):
#     page.goto("/visibility")
#     page.click('#hideButton')
#     assert page.is_hidden('#removedButton')
#     assert page.is_hidden('#zeroWidthButton')
#     assert page.is_hidden('#overlappedButton')
#     assert page.is_hidden('#transparentButton')
#     assert page.is_hidden('#invisibleButton')
#     assert page.is_hidden('#notdisplayedButton')
#     assert page.is_hidden('#offscreenButton')
    
def test_sample_app(page):
    page.goto("/sampleapp") 
    page.fill('//input[@name="UserName"]', 'Test')
    page.fill('//input[@name="Password"]', 'psd') 
    page.click('#login')
    assert page.inner_text('#loginstatus') == "Invalid username/password"
    page.fill('//input[@name="UserName"]', 'Test')
    page.fill('//input[@name="Password"]', 'pwd') 
    page.click('#login')
    assert page.inner_text('#loginstatus') == "Welcome, Test!"
    page.click('#login')
    assert page.inner_text('#loginstatus') == "User logged out."
    
def test_mouse_over(page):
    page.goto("/mouseover")
    page.dblclick('//*[@title="Click me"]')
    assert page.inner_text('#clickCount') == "2"
    
def test_non_breaking_space(page):
    page.goto("/nbsp")
    page.click("text='My Button']")
    
    

    
    
    

    

    
    
    
