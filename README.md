# OYK-Python-2022


# Sanal Makina Komutlari
```shell

# Sanal Makinayi baslat
vagrant up

# Sanal Makinayi durdur
vagrant halt

# Sanal Makinayi sil
vagrant destroy
```

# Python icin paket kurulumu
```shell
pipenv install [paket-adi]
```


# Ogrenilmesi Gerekenler
* Python
* Django
* Git

### ui dosyalarini python dosyasina cevirme
```shell
pyside2-uic [ui-dosya adi].ui -o [python-dosya adi].py
```

-------
## Paketleme

* Pipfile duzenlendi pyinstaller eklendi.
* kurulumu yapmak icin proje icinde vscode terminalden pipenv install komutunu girin.

### yazilim paketleme icin kurulmasi gereken paket
```shell
sudo apt install python3.9-dev
```

### yazilim paketleme
```shell
pyinstaller 10_crypto_api.py --onefile --windowed
```


# Django

* Django kurulumu
```shell
cd Desktop
mkdir django-projesi
cd django-projesi
pipenv install django
code .
pipenv shell
```

* django proje baslatma
```shell
django-admin startproject config .
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```