from selenium.webdriver.common.by import By


class Locators:
    EMAIL_FIELD_LOGIN_PAGE = (By.XPATH, "//input[@type='text']")  # поле "Email" на странице входа
    PASSWORD_FIELD_LOGIN_PAGE = (By.XPATH, ".//input[@type='password']")  # поле "Пароль" на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти" на странице входа
    ORDER_HISTORY_BUTTON = (By.XPATH, '//a[contains(text(), "История заказов")]')  # кнопка "История заказов"
    LOGOUT_BUTTON = (By.XPATH, "//button[@type='button' and contains(@class, 'Account_button') and contains(@class, 'text_color_inactive') and text()='Выход']")  # кнопка "Выход" в личном кабинете

    REPAIR_PASSWORD_BUTTON_LOGIN_PAGE = By.XPATH, '//a[text() = "Восстановить пароль"]'  # Кнопка "Восстановить пароль" на экране входа
    EMAIL_FIELD = (By.CLASS_NAME, 'input__textfield') # Поле email
    REPAIR_PASSWORD_BUTTON_RECOVERY_PAGE = (By.CLASS_NAME, 'button_button__33qZ0') # Кнопка "Восстановить" на странице восстановления пароля
    SHOW_PASSWORD_BUTTON = (By.CSS_SELECTOR, '.input__icon')# Кнопка показать/скрыть пароль
    SAVE_BUTTON = (By.XPATH, '//button[text()="Сохранить"]')  # кнопка "Сохранить"

    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, '//p[text()="Личный Кабинет"]')  # кнопка "Личный кабинет"
    FORGOT_PASSWORD_BUTTON_LOGIN_PAGE = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]')  # кнопка "Восстановить пароль"
    EMAIL_FIELD_REPAIR_PASSWORD_PAGE = (By.CLASS_NAME, 'input__textfield')#поле email на странице восстановления пароля
    REPAIR_BUTTON = (By.XPATH, '//button[text()="Восстановить"]') #кнопка "Восстановить" на странице восстановления пароля

    CONSTRUCTOR_BUTTON = (By.XPATH, '//li/a[@href="/"]')  # кнопка "Конструктор"
    FEED_BUTTON = (By.XPATH, '//p[text()="Лента Заказов"]') # Лента заказов
    FLUOR_BUN = (By.XPATH, '//p[text()="Флюоресцентная булка R2-D3"]') # Ингредиент флюоресцентная булка
    INGREDIENT_DETAILS_WINDOW = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]') # Всплывающее окно с деталями
    CLOSE_DETAILS_WINDOW_BUTTON = (By.XPATH, '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]') # Кнопка закрытия всплывающего окна с деталями ингредиента (крестик)
    ADDED_INGREDIENT_COUNTER = (By.XPATH, '//ul[1]/a[1]//p[contains(@class, "num")]') # Каунтер ингредиента флюоресцентная булка
    BASKET = (By.XPATH, "//span[@class='constructor-element__text' and text()='Перетяните булочку сюда (верх)']") #корзина (конструктор) с выбранными инредиентами
    MAKE_ORDER_BUTTON = (By.XPATH, '//button[contains(text(), "Оформить заказ")]') # кнопка "Оформить заказ"
    ORDER_ID_IN_ORDER_WINDOW = (By.XPATH, "//p[@class='undefined text text_type_main-medium mb-15' and text()='идентификатор заказа']") # строка "Идентификатор заказа" в окне нового заказа
    TEXT_ORDER_IN_WORK = (By.XPATH, '//p[text()="Ваш заказ начали готовить"]') # строка "Ваш заказ начали готовить" в окне нового заказа
    ID_9999 = (By.XPATH, f"//*[contains(text(), '{9999}')]") # идентификатор заказа, который виден до момента загрузки номера нового заказа


    ACTIVE_PASSWORD_FIELD_RESET_PASSWORD_PAGE = (By.CSS_SELECTOR, 'div.input_status_active') #Подсвечиваемое поле пароль после нажатия на "Показать пароль"
    TITLE_RESET_PASSWORD_PAGE = (By.XPATH, '//h2[text()="Восстановление пароля"]') # заголовок "Восстановление пароля"

    FIRST_ORDER_IN_HISTORY_FEED_PAGE = (By.XPATH, "//li[contains(@class, 'OrderHistory_listItem') and contains(@class, 'mb-6')]") # первый заказ в ленте заказов
    ORDER_DETAILS_POPUP = (By.XPATH, "//div[contains(@class, 'Modal_orderBox') and contains(@class, 'Modal_modal__contentBox')]") # попап с деталями заказа
    CLOSE_ORDER_DETAILS_POPUP = (By.XPATH, '//section[contains(@class, ''"Modal_modal_opened")]//button[contains(@class, "close")]') # кнопка закрытия окна с деталями заказа
    ALL_ORDERS_FEED_PAGE = (By.XPATH, ".//div[@class='OrderHistory_textBox__3lgbs mb-6']//p[@class='text text_type_digits-default']") # список всех заказов из ленты заказов
    ORDER_STRUCTURE = (By.XPATH, '//p[text()="Cостав"]') # заголовок "Состав" в карточке заказа
    TITLE_FEED = (By.XPATH, '//h1[text()="Лента заказов"]') # заголовок "Лента заказов"
    TITLE_ALL_TIME_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']") # заголовок "Выполнено за все время"
    TITLE_DAILY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']") # заголовок "Выполнено за сегодня"
    NUMBER_OF_ORDER_IN_WORK = (By.XPATH, "//li[contains(text(), '0')]") # номер заказа в работе
    ALL_ORDERS_DONE = (By.XPATH, "//li[text()='Все текущие заказы готовы!']") # строка "Все текущие заказы готовы"
    COUNTER_DAILY_ORDERS = (By.XPATH, "//p[contains(., 'Выполнено за сегодня:')]/following-sibling::p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]") # счетчик "Выполнено за сегодня"
    COUNTER_ALL_ORDERS = (By.XPATH, "//p[contains(., 'Выполнено за все время:')]/following-sibling::p[contains(@class, 'OrderFeed_number') and contains(@class, 'text_type_digits-large')]") # счетчик "Выполнено за все время"
    FIRST_USER_ORDER = (By.CLASS_NAME, 'OrderHistory_link__1iNby') # карточка первого заказа в списке пользователя
    FIRST_USER_ORDER_ID = (By.XPATH, '//div[contains(@class, "OrderHistory_textBox")]/p[contains(@class, "text_type_digits-default")]') # номер первого заказа в списке пользователя
    ORDER_NUMBER_LIST = (By.CSS_SELECTOR, ".Order_number__item") # список с номерами заказов
    OVERLAY = (By.CSS_SELECTOR, 'div.Modal_modal_overlay__x2ZCr') # перекрывающий фон
    NEW_ORDER_NUMBER = (By.XPATH, '//h2[contains(@class, "Modal_modal__title__") and contains(@class, "text_type_digits-large mb-8")]') # номер нового заказа
    LOADING_ANIMATION = (By.CLASS_NAME, 'Modal_modal__loading__3534A') # анимация ожидания до загрузки страницы

    USER_ORDERS_LIST = (By.XPATH, "//div[contains(@class, 'OrderHistory_textBox__3lgbs')]/p[contains(@class, "
                                       "'text_type_digits-default')]") # список заказов пользователя


    LOGIN_BUTTON_MAIN_PAGE = (By.XPATH, '//button[text()="Войти в аккаунт"]') #кнопка "Войти в аккаунт" на главной странице
    NAME_FIELD_REGISTRATION_PAGE = (By.XPATH, '//label[text()="Имя"]/following-sibling::input') #поле "Имя" на странице регистрации
    EMAIL_FIELD_REGISTRATION_PAGE = (By.XPATH, '//label[text()="Email"]/following-sibling::input') #поле "Email" на странице регистрации
    PASSWORD_FIELD_REGISTRATION_PAGE = (By.NAME, 'Пароль') #поле "Пароль" на странице регистрации
    REGISTRATION_BUTTON_REGISTRATION_PAGE = (By.XPATH, '//button[text()="Зарегистрироваться"]') # кнопка "Зарегистрироваться" на странице регистрации


    FORGOT_PASSWORD_BUTTON = (By.XPATH, '//a[contains(text(), "Восстановить пароль")]') #кнопка "Восстановить пароль"
    LOGIN_BUTTON_FORGOT_PASSWORD_PAGE = (By.XPATH, '//a[contains(text(), "Войти")]') #кнопка "Войти" на странице восстановления пароля

