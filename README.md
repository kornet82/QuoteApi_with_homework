# Развертывание на локальной машине
1. Создаем виртуальное окружение: python3 -m venv flask_venv
1. Активируем venv: source flask_venv/bin/activate
1. Устанавливаем зависимости: pip install -r requirements.txt
1. Создаем локальную БД: flask db upgrade

### После клонирования с чужого репо:
1. $ git clone https://github.com/......
2. Нужно удалить ссылки на чужой репо:
3. Проверяем командой $ git remote -v
4. Удаляем командой $ git remote rm origin
5. Добавляем свой: $ git remote add origin git@github......
6. git add .
7. git commit -m "First commit"
8. git push -u origin main