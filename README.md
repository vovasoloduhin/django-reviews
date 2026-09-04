# Django Product Reviews

Проект Django для перегляду продуктів і подачі відгуків.

## Запуск

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Відкрийте `http://127.0.0.1:8000/`.

## Маршрути

- `/` — список продуктів.
- `/products/<id>/` — детальна сторінка продукту та форма відгуку.
- `/admin/` — админ панель для додавання продуктів.

## Коміти

Під час виконання зроблено окремі коміти для ініціалізації, моделей, форм/views, шаблонів та фінального налаштування.

## Моделі
Product і Review models знаходяться в `reviews/models.py`.

## Форма перегляду
Сторінка детальної інформації перевіряє оцінки в діапазоні від 1 до 5 і зберігає відгуки за допомогою запиту POST.

## Templates
У комплект входять адаптивні шаблони для списку товарів і сторінки з детальною інформацією про товар.

## Підсумковий контрольний список
- Product list route
- Product detail route
- Review creation
- Review display
- Admin registration
