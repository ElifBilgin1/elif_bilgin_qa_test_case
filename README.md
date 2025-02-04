# Insider UI Test Automation

Bu proje, Insider web sitesinin UI test otomasyonunu içermektedir.

## Gerekli Python kütüphanelerini kurun:

```
pip install -r requirements.txt
```

## Testleri Çalıştırma

Testleri çalıştırmak için aşağıdaki komutu kullanın:

```
python -m unittest tests/UITest.py -v
```

## Test Senaryosu

Test aşağıdaki adımları içermektedir:

1. Insider ana sayfasını ziyaret etme
2. Careers sayfasına gitme
3. QA pozisyonlarını filtreleme
4. İş ilanlarını kontrol etme
