# Setting Up Python3, Selenium, Behave, and Allure for Automation Testing

## Prerequisites
Ensure you have the following installed on your system:
- macOS, Windows, or Linux
- Python 3.7+
- Google Chrome & ChromeDriver (for Selenium WebDriver)
- Java (for Allure Report generation)

---

## 1. Install Python3
### **macOS (via Homebrew):**
```bash
brew install python3
```

### **Windows:**
Download and install Python from [python.org](https://www.python.org/downloads/).

### **Verify Installation:**
```bash
python3 --version
```

---

## 2. Set Up a Virtual Environment
```bash
python3 -m venv automation_env
source automation_env/bin/activate  # macOS/Linux
automation_env\Scripts\activate  # Windows
```

---

## 3. Install Selenium
```bash
pip install selenium
```

### **Verify Installation:**
```python
python3 -c "import selenium; print(selenium.__version__)"
```

---

## 4. Install Behave
```bash
pip install behave
```

### **Verify Installation:**
```bash
behave --version
```

---

## 5. Install ChromeDriver
### **macOS:**
```bash
brew install chromedriver
```
### **Windows:**
Download from [ChromeDriver](https://sites.google.com/chromium.org/driver/) and add it to your system PATH.

### **Verify Installation:**
```bash
chromedriver --version
```

---

## 6. Install Allure for Test Reporting
### **Install Allure CLI:**
#### **macOS (via Homebrew):**
```bash
brew install allure
```

#### **Windows (via Scoop):**
```bash
scoop install allure
```

### **Verify Installation:**
```bash
allure --version
```

### **Install Allure Pytest Adapter:**
```bash
pip install allure-behave
```

---

## 7. Running a Sample Test
Create a new directory for your project and add the following structure:
```
project_folder/
│── features/
│   ├── example.feature
│   ├── steps/
│   │   ├── steps.py
│── environment.py
```

### **`features/example.feature`**
```gherkin
Feature: Sample Test
  Scenario: Open Google
    Given I open the browser
    When I navigate to "https://www.google.com"
    Then I should see "Google"
```

### **`features/steps/steps.py`**
```python
from selenium import webdriver
from behave import given, when, then

@given('I open the browser')
def open_browser(context):
    context.driver = webdriver.Chrome()

@when('I navigate to "{url}"')
def navigate_to_url(context, url):
    context.driver.get(url)

@then('I should see "{text}"')
def verify_text(context, text):
    assert text in context.driver.title
    context.driver.quit()
```

### **Run Tests with Behave:**
```bash
behave
```

### **Generate Allure Report:**
```bash
behave -f allure_behave.formatter:AllureFormatter -o reports/
allure serve reports/
```

---

## Setup Complete!
You’re now ready to write and run Selenium automation tests with Behave and Allure Reporting.

