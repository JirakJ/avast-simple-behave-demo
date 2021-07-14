import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support.select import Select

@given(u'launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="/Users/jirakj/work/drivers/chromedriver")

@when(u'open avast homepage')
def step_impl(context):
    context.driver.get("https://avast.com")

@then(u'go to eshop page')
def step_impl(context):
    element = "//a[@data-cta='homeShop']"
    context.driver.find_element_by_xpath(element).click()

@then("choose just for one PC in {cell}")
def step_impl(context, cell):
    """
    :type context: behave.runner.Context
    :type cell: str
    """
    element = '//*[@id="allProducts-tab"]/section[1]//table//tfoot//td['+cell+']//select'
    select = Select(context.driver.find_element_by_xpath(element))
    select.select_by_index(1)

@then(u'click on buy in {cell}')
def step_impl(context, cell):
    """
    :type context: behave.runner.Context
    :type cell: str
    """
    element = '//*[@id="allProducts-tab"]/section[1]//table//tfoot//td['+cell+']//a[@data-role="cart-link"]'
    context.driver.find_element_by_xpath(element).click()


@then("fill {name}, {surname} and {email}")
def step_impl(context,name, surname, email):
    """
    :type context: behave.runner.Context
    :type name: str
    :type surname: str
    :type email: str
    """
    context.driver.find_element_by_id("order_type_customer_name").send_keys(name)
    context.driver.find_element_by_id("order_type_customer_surname").send_keys(surname)
    context.driver.find_element_by_id("order_type_customer_email").send_keys(email)

@then(u'click on continue')
def step_impl(context):
    context.driver.find_element_by_xpath("//div[@class='b-navigation']//input[@type='submit']").click()

@then("fill in {cardNumber}, {expireMonth}, {expireYear}, {cvv}")
def step_impl(context, cardNumber, expireMonth, expireYear, cvv):
    """
    :type context: behave.runner.Context
    :type cardNumber: str
    :type expireMonth: str
    :type expireYear: str
    :type cvv: str
    """
    time.sleep(3)
    context.driver.find_element_by_id("CardNumber").send_keys(cardNumber)
    context.driver.find_element_by_id("ExpireMonth").send_keys(expireMonth)
    context.driver.find_element_by_id("ExpireYear").send_keys(expireYear)
    context.driver.find_element_by_id("CVV").send_keys(cvv)


@then("close cookie modal by click on OK")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.find_element_by_xpath('//*[@id="onetrust-accept-btn-handler"]').click()


@then("close browser")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    context.driver.quit()