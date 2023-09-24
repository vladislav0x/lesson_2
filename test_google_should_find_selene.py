from selene.support.shared import browser
from selene import be, have


def test_search():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser'))


def test_search_second():
    browser.element('[name="q"]').should(be.blank).type('Шла1Саша2По3шоссе4и5сосала5сушку').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))

    print("Поиск не дал результатов!")
