class TestData:
    EMAIL_FOR_LOGIN = 'lucky777@ya.ru'
    PASSWORD_FOR_LOGIN = '123456'


    ingredients_for_order = {"ingredients": ["61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa72", "61c0c5a71d1f82001bdaaa6f"]}

class URLs:
    BASE_URL = 'https://stellarburgers.nomoreparties.site/'
    FORGOT_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/forgot-password'
    RESET_PASSWORD_PAGE = 'https://stellarburgers.nomoreparties.site/reset-password'
    ORDER_HISTORY_PAGE = 'https://stellarburgers.nomoreparties.site/account/order-history'
    PERSONAL_ACCOUNT_PAGE = 'https://stellarburgers.nomoreparties.site/account/profile'
    LOGIN_PAGE = 'https://stellarburgers.nomoreparties.site/login'
    FEED_PAGE = 'https://stellarburgers.nomoreparties.site/feed'
    REGISTRATION_PAGE = 'https://stellarburgers.nomoreparties.site/register'

class Endpoints:
    CREATE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/register'
    LOGIN_USER = 'https://stellarburgers.nomoreparties.site/api/auth/login'
    CHANGE_USER_DATA = 'https://stellarburgers.nomoreparties.site/api/auth/user'
    CREATE_ORDER = 'https://stellarburgers.nomoreparties.site/api/orders'
    GET_USER_ORDERS = 'https://stellarburgers.nomoreparties.site/api/orders'
    DELETE_USER = 'https://stellarburgers.nomoreparties.site/api/auth/user'
