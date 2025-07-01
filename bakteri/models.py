from django.db import models

class KategoriBakteri(models.Model):
    nama = models.CharField(max_length=100)

    def __str__(self):
        return self.nama

class Bakteri(models.Model):
    nama = models.CharField(max_length=100)
    nama_ilmiah = models.CharField(max_length=200)
    bentuk = models.CharField(max_length=100)
    cara_berkembang_biak = models.TextField()
    gambar = models.ImageField(upload_to='gambar_bakteri/')
    referensi = models.URLField()
    kategori = models.ForeignKey(KategoriBakteri, on_delete=models.CASCADE)

    def __str__(self):
        return self.nama
