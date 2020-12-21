# Лабораторная работа 8

## Установка

```bash
git clone https://github.com/assisken/highload-hw-8
cd highload-hw-8
sudo pip3 install -r requirements.txt
```

## Запуск

```bash
chmod +x ./start.sh
./start.sh

# Подождите, когда создастся топики main_topic и dead_letter

python app/consumer.py
python app/dead_letter_consumer.py
python app/produser.py
```
