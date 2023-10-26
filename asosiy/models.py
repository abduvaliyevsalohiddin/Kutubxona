from django.db import models

JINS = [
    ("Erkak", "Erkak"),
    ("Ayol", "Ayol"),
]

JANR = [
    ("Badiiy", "Badiiy"),
    ("Ilmiy", "Ilmiy"),
    ("Hikoya", "Hikoya"),
    ("Roman", "Roman"),
    ("Ertak", "Ertak"),
]


class Talaba(models.Model):
    ism = models.CharField(max_length=30)
    kurs = models.PositiveSmallIntegerField()
    kitob_soni = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.ism}"


class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    jins = models.CharField(max_length=6, blank=True, choices=JINS)
    tugulgan_kun = models.DateField()
    kitoblar_soni = models.PositiveSmallIntegerField()
    tirik = models.BooleanField()

    def __str__(self):
        return f"{self.ism}"


class Kitob(models.Model):
    nom = models.CharField(max_length=50)
    janr = models.CharField(max_length=20, choices=JANR)
    sahifa = models.PositiveSmallIntegerField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}"


class Kutubxonachi(models.Model):
    ism = models.CharField(max_length=30)
    ish_vaqti = models.PositiveSmallIntegerField(verbose_name=" necha soat")

    def __str__(self):
        return f"{self.ism}"


class Record(models.Model):
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob = models.ForeignKey(Kitob, on_delete=models.CASCADE)
    kutubxonachi = models.ForeignKey(Kutubxonachi, on_delete=models.CASCADE)
    olingan_sana = models.DateTimeField(auto_now_add=True)
    qaytardi = models.BooleanField(default=False)
    qaytarish_sana = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.kutubxonachi} --> {self.talaba} --> {self.kitob}"
