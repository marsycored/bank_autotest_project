# Учебный проект тестирования 
Название/Описание

# Требования
requirements.txt 
Установка требований 

# Установка (CI or GIT)
Процесс подключения к репозиторию

# Запуск тестов
Команда запуска: 
pytest test/ --alluredir=result


# Контакты
Тим лид: Михаил 
Ответственный по проекту: Дарья

# Структура\Архитектура проекта
`/test_repo                          # репозиторий проекта 
    /test_project                   # папка проекта
        /page                       # page object модели
            __init__.py
            base_page_py            # базовый класс
            login_page.py           # класс модуля
        /data                       # тестовые данные и локаторы
            /locators               # селекторы и элементы 
                /login_locators.py  # селекторы элементов модулей
            /values                 # тестовые данные 
                login_values.py     # тестовые данные модуля
        /tests                      # тестовые сценарии 
            __init__.py             
            /smoke                  # дым
                test_login.py       
            /accept                 # приемка
                test_module.py      
            /api                    # апи \ бэк
                test_auth.py
            /load                   # нагрузочное
                locust_smoke.py
        /config                     # конфигурация 
            environments.py         # настройка стендов / окружения
            pytest.ini              # конфигурация тестов 
        /units                      # вспомогательные инструменты 
            __init__.py             
            /drivers                # 
            actions.py              #
            asserts.py              #
            helpers.py              #
        /docs                       # 
            UPDATE.md               # процесс обновления
            TESTCASES.md            # описание кейсов
conftest.py                         # фикстуры pytest 
requiroments.txt                    # зависимости 
README.md                           # описание проекта 
`
* Модули: 
1) Логин
            