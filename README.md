# GitHub Actions Test Projesi

Bu proje, GitHub Actions workflow'larını test etmek için oluşturulmuş basit bir Python projesidir.

## Proje Yapısı

- `calculator.py`: Basit hesap makinesi fonksiyonları
- `test_calculator.py`: Pytest ile yazılmış birim testleri
- `.github/workflows/test.yml`: GitHub Actions workflow dosyası

## Kurulum

```bash
pip install -r requirements.txt
```

## Testleri Çalıştırma

```bash
pytest test_calculator.py -v
```

## GitHub Actions

Bu proje, her push ve pull request'te otomatik olarak testleri çalıştıran bir GitHub Actions workflow'u içerir.

