import pytest
from api import PetFriends
from settings import valid_email, valid_password

# Создаем экземпляр класса PetFriends
pf = PetFriends()


# Пример параметризации для теста добавления питомца
@pytest.mark.parametrize("name, animal_type, age", [
    pytest.param("Фрикаделька", "Котик", "5", id="test_frikadelka"),
    pytest.param("Коша", "Котенок", "5", id="test_koshka"),
    pytest.param("Мурка", "Кошка", "13", id="test_murka"),
    pytest.param("Пушистик", "Кот", "3", id="test_pushistik")
])
def tests_post_add_new_pet(name, animal_type, age):
    print('Тестовый метод POST- добавляем  питомцев и проверяем добавление')
    # Получаем ключ авторизации
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    result,status  = pf.add_new_pet(auth_key, name, animal_type, age)

    # Проверки
    if status != 200:
        print(f"Ошибка: получен статус {status} вместо 200")
        return  # Завершаем тест при ошибке статуса

    # Проверяем данные питомца
    if result.get('name') != name:
        print(f"Ошибка: имя не совпадает. Ожидалось {name}, получено {result.get('name')}")
        return

    if result.get('animal_type') != animal_type:
        print(f"Ошибка: тип животного не совпадает. Ожидалось {animal_type}, получено {result.get('animal_type')}")
        return

    if result.get('age') != age:
        print(f"Ошибка: возраст не совпадает. Ожидался {age}, получен {result.get('age')}")
        return

    # Проверяем наличие обязательных полей
    required_fields = ['_id', 'id', 'created_at', 'user_id']
    for field in required_fields:
        if field not in result:
            print(f"Ошибка: отсутствует поле {field}")
            return

    print("Тест пройден успешно!")

   
#tests_post_add_new_pet()