from enum import Enum

from pages.registration_page import RegistrationPage


class Gender(Enum):
    MALE = 1
    FEMALE = 2
    OTHER = 3


class Hobby(Enum):
    SPORTS = 1
    READING = 2
    MUSIC = 3


def test_demo_qa_form(browser_window):
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Vasilisa')
    registration_page.fill_last_name('Pupkina')
    registration_page.fill_email('vpupkina@gmail.com')
    registration_page.choose_gender(Gender.FEMALE)
    registration_page.fill_mobile('88005553322')
    registration_page.fill_date_of_birth('2007-08-16')
    registration_page.fill_subjects("Chemistry")
    registration_page.choose_hobby(Hobby.MUSIC)
    registration_page.upload_picture('test_demoqa/resources/pic.png')
    registration_page.fill_current_address('some address')
    registration_page.select_state('NCR')
    registration_page.select_city('Delhi')
    registration_page.submit_form()
    registration_page.should_have_elements('Vasilisa Pupkina',
                                           'vpupkina@gmail.com',
                                           'Female',
                                           '8800555332',
                                           '16 August,2007',
                                           'Chemistry',
                                           'Music',
                                           'pic.png',
                                           'some address',
                                           'NCR Delhi'
                                           )