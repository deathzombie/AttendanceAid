# main.py

from flask import Flask, render_template, request, redirect
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from routes import combination_to_url  # Import the dictionary

app = Flask(__name__)


# Define your automation function
def perform_web_automation(username, password, target_url):
    # Your existing web automation code goes here
    # It logs in to the college's website and performs the desired actions

    webdriver_path = "C:/chromedriver-win32 (1)/chromedriver-win32/chromedriver.exe"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.executable_path = webdriver_path

    browser = webdriver.Chrome(options=chrome_options)

    website_url = "https://lms.thapar.edu/moodle/login/index.php"
    browser.get(website_url)

    username_field = WebDriverWait(browser, 10).until(
        ec.visibility_of_element_located((By.ID, "username"))
    )

    password_field = browser.find_element(By.ID, "password")

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = browser.find_element(By.ID, "loginbtn")
    login_button.click()

    # Use the target_url determined by the routes.py file
    browser.get(target_url)


@app.route('/')
def index():
    return render_template('main.html')


def determine_target_url(branch, subgroup, course_name):
    # Create a tuple representing the combination
    combination = (branch, subgroup, course_name)

    # Check if the combination exists in the dictionary
    if combination in combination_to_url:
        return combination_to_url[combination]
    else:
        # If the combination is not found, return the default URL
        return "https://google.com"


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Get form data
        branch = request.form.get('branch')
        subgroup = request.form.get('subgroup')
        course_name = request.form.get('courses')

        # Determine the target URL based on the combination
        target_url = determine_target_url(branch, subgroup, course_name)

        # Call your web automation function with the determined target URL
        username = "rsharma7_be22@thapar.edu"
        password = "RAJ25371#lms"
        perform_web_automation(username, password, target_url)

        # Redirect to the form after submission
        return redirect('/')
    else:
        # Handle GET request (show the form)
        return render_template('main.html')


if __name__ == '__main__':
    app.run(debug=True)
