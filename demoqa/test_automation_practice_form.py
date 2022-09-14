from selene.support.shared import browser
from demoqa.variables import web, year, month, day, abs_path
from selene import have

#browser.config.hold_browser_open = True


def test_student_registration_form():
    browser.open(web + 'automation-practice-form')
    browser.element('[id="firstName"]').type('Тест')
    browser.element('[id="lastName"]').type('Тестов')
    browser.element('[id="userEmail"]').type('test@test.test')
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[id="userNumber"]').type(89159999999)
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element(year).element('[value="1996"]').click()
    browser.element(month).element('[value="7"]').click()
    browser.element(day).click()
    browser.element('[id="subjectsInput"]').type('Accounting').press_enter() \
        .type('Economics').press_enter()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[id="uploadPicture"]').send_keys(abs_path('../files_for_test/test.png'))
    browser.element('[id="currentAddress"]').type('Россия, Москва')
    browser.element('[id="react-select-3-input"]').type('Haryana').press_enter()
    browser.element('[id="react-select-4-input"]').type('Karnal').press_enter()
    browser.element('[id="submit"]').click()
    # проверки
    browser.all('table tr')[1].all('td')[1].should(have.exact_text('Тест Тестов'))
    browser.all('table tr')[2].all('td')[1].should(have.exact_text('test@test.test'))
    browser.all('table tr')[3].all('td')[1].should(have.exact_text('Female'))
    browser.all('table tr')[4].all('td')[1].should(have.exact_text('8915999999'))
    browser.all('table tr')[5].all('td')[1].should(have.exact_text('08 August,1996'))
    browser.all('table tr')[6].all('td')[1].should(have.exact_text('Accounting, Economics'))
    browser.all('table tr')[7].all('td')[1].should(have.exact_text('Music, Sports'))
    browser.all('table tr')[8].all('td')[1].should(have.exact_text('test.png'))
    browser.all('table tr')[9].all('td')[1].should(have.exact_text('Россия, Москва'))
    browser.all('table tr')[10].all('td')[1].should(have.exact_text('Haryana Karnal'))