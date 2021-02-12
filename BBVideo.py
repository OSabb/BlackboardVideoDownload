from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


USERNAME = "SABBAGHO@UWINDSOR.CA"
PASSWORD = "Uwindsor#1!"



driver = webdriver.Chrome(ChromeDriverManager().install())
actions = ActionChains(driver) 
driver.get("https://blackboard.uwindsor.ca/webapps/login/")
time.sleep(.5)
driver.find_element_by_class_name("button-1").click()
driver.find_element_by_class_name("centerloginbtn").click()
driver.get("https://login.microsoftonline.com/12f933b3-3d61-4b19-9a4d-689021de8cc9/saml2?SAMLRequest=fZJRb9sgFIX%2FCuId2%2BA4MyhOlbaqFqlTo9rdw14qDCRBsyHj4mw%2Ff8xN1O6lL0iIe865936sbv6MAzqbANa7BtOswMg45bV1hwa%2FdA%2BkxjfrFchxYCexmeLRPZtfk4GIktCBeHtp8BSc8BIsCCdHAyIq0W6%2BPQqWFeIUfPTKDxhtAEyIKerOO5hGE1oTzlaZl%2BfHBh9jPIHI836Q6mfvZdDZ9Ns6DT5kSuYyhZN%2Fcfl8tO1TLgcrIX%2Bli1eK0X1qyjoZ50GuXoM%2FWJeNVgUPfh%2B9G6wzmfJjTtmel2VfklIvKVn0lBMuF5osa14wqk2tFJ%2BTGEYPPigzD9%2FgvRzAYLS9b7Asl6ZQVV9qXmlalfSoi4JyWfPDl32ZdFvYSQB7Nu8ygMlsHUTpYoNZSiIFI5R1lAlWiYpmtOY%2FMNpdVnab5p9RfLbf%2Fq0IxNeu25HdU9th9P2KNBXgC0Axp4eP5D43lldceP0OhSScepV%2FdFxfrv%2F%2FkPVf&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=m1XtEzpoGdO6Bu5qMsY9OZmxP6%2BWxv9Mu%2FQ8DqUBxezsACcDERiDHD%2BQOd9aSxbienZak5IYwUH3wLqFzsfPsNu6G9CNIkJvm3qSHeH524V5oX13vGB6lSQZf98cbDoKEmXY3LDR6AiBNTgK%2FoOVq2CJNpcSCVj69JaxSKZ3PjxIW%2BgXuWMei4rOKW4BCF9iQ8Jlttd0PeXfRmdyK8lI8hjnBnL8xo%2F762Lvss2nBuTRUXdV0jKuv0g1mwrTNqdvnUKMMhJ19gTmpKmo1HD7OUZC7dQNasFRyiazhW20Uib7cLKNAgFUmfQoHAor5%2FUoVBKvAYZD%2B%2FMBebtiZsgOtQ%3D%3D&sso_reload=true")
time.sleep(.5)
driver.find_element_by_xpath("//*[@id='i0116']").click()
driver.find_element_by_xpath("//*[@id='i0116']").send_keys(USERNAME)


time.sleep(10)
#driver.quit()