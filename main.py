import time
from telnetlib import EC

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

chrome_driver_path = "/Users/immom/Downloads/chromedriver_win32/chromedriver"
driver = webdriver.Chrome(service=Service(chrome_driver_path))
print("Current session is {}".format(driver.session_id))
try:
    driver.get("https://www.cybercoders.com/search/?searchterms=python&searchlocation=19736&newsearch=true&originalsearch=true&sorttype=")
except Exception as e:
    print(e.message)

Login_button = driver.find_element(By.CLASS_NAME, "open-login")
Login_button.click()
driver.implicitly_wait(20)
""""
try:
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "email-input"))
    )
    email_field.send_keys("login.docplus@gmail.com")

    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Password"))
    )
    password_field.send_keys("software124$")
    password_field.send_keys(Keys.ENTER)
finally:
    driver.close()
    
subject = "An email with attachment from Python"
body = "This is an email with attachment sent from Python"
sender_email = "my@gmail.com"
receiver_email = "your@gmail.com"
password = input("Type your password and press enter:")

# Create a multipart message and set headers
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message["Bcc"] = receiver_email  # Recommended for mass emails
"""
email_field = driver.find_element(By.CLASS_NAME, "email-input")
email_field.send_keys('login.docplus@gmail.com')
driver.implicitly_wait(10)

password_field = driver.find_element(By.ID, "Password")
password_field.send_keys('software124$')
driver.implicitly_wait(10)
password_field.send_keys(Keys.ENTER)
time.sleep(5)

all_listing = driver.find_elements(By.CLASS_NAME, "job-listing-item")

for listing in all_listing:
    print("called")
    time.sleep(2)
    try:
        apply_now_button = driver.find_element(By.LINK_TEXT, "Apply Now")
        apply_now_button.click()
        time.sleep(2)
        apply_button = driver.find_element(By.LINK_TEXT, "Apply")
        apply_button.click()
        time.sleep(2)
        finish_button = driver.find_element(By.ID, "btn-submit")
        finish_button.click()
        '''
        email_link = driver.find_element(By.LINK_TEXT, "Email me to apply for this position")
        email_link.click()
        message.attach(MIMEText(body, "plain"))
        
        filename = "Manish Kothary -Cheif Technology officer Resume.pdf"
        
        
        with open(filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
          
        encoders.encode_base64(part)
        
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        
        message.attach(part)
        text = message.as_string()
        
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, text)
        '''
    except NoSuchElementException:
        print("No application button, skipped...")
        continue
    except TimeoutException:
        print("completed")
        break

driver.close()