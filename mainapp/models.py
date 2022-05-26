from django.db import models


class Synonym(models.Model):
    word = models.CharField(max_length=100)


class Antonym(models.Model):
    word = models.CharField(max_length=100)


class Hyponym(models.Model):
    word = models.CharField(max_length=100)


class Hyperonym(models.Model):
    word = models.CharField(max_length=100)


class InfoAdjective(models.Model):
    ADJECTIVES_TYPES_TWO = (
        ("asliy_sifat", "Asliy sifat"),
        ("nisbiy_sifat", "Nisbiy sifat"),
    )

    ADJECTIVE_TYPES = (
        ("xususiyat", "Xususiyat sifatlari"),
        ("rang_tus", "Rang – tus sifatlari"),
        ("maza_tam", "Maza – ta’m sifatlari"),
        ("hajm_olchov", "Hajm – o’lchov sifatlari"),
        ("hid", "Hid sifatlari"),
        ("makon_zamon", "Makon-zamon sifatlari"),
    )

    ADJECTIVE_LEVELS = (
        ("oddiy", "Oddiy"),
        ("orttirma", "Orttirma"),
        ("ozaytirma", "Ozaytirma"),
        ("qiyosiy", "Qiyosiy"),
    )

    ADJECTIVE_TYPE_STRUCTURE = (
        ("sodda_tub", "Sodda tub"),
        ("sodda_yasama", "Sodda yasama"),
        ("qoshma", "Qo'shma"),
        ("juft", "Juft"),
        ("takroriy", "Takroriy"),
    )

    word = models.CharField(max_length=100, unique=True)
    adjectives_two = models.CharField(max_length=15, choices=ADJECTIVES_TYPES_TWO, default=ADJECTIVES_TYPES_TWO[0][0])
    adjective_type = models.CharField(max_length=15, choices=ADJECTIVE_TYPES, default=ADJECTIVE_TYPES[0][0])
    adjective_level = models.CharField(max_length=15, choices=ADJECTIVE_LEVELS, default=ADJECTIVE_LEVELS[0][0])
    adjective_type_structure = models.CharField(max_length=15, choices=ADJECTIVE_TYPE_STRUCTURE, default=ADJECTIVE_TYPE_STRUCTURE[0][0])
    review = models.CharField(max_length=1000)
    synonym = models.ManyToManyField(Synonym, blank=True)
    antonym = models.ManyToManyField(Antonym, blank=True)
    hyponym = models.ManyToManyField(Hyponym, blank=True)
    hyperonym = models.ManyToManyField(Hyperonym, blank=True)

    def __str__(self):
        return self.word

class InfoNoun(models.Model):
    NOUN_TYPES = (
        ("shaxs", "Shaxs otlar"),
        ("narsa", "Narsa otlar"),
        ("orin_joy", "O'rin-joy otlar"),
        ("faoliyat", "Faoliyat-otlari"),
    )

    NOUN_TYPES_STRUCTURE = (
        ("sodda", "Sodda"),
        ("qoshma", "Qo'shma"),
        ("juft", "Juft"),
        ("takroriy", "Takroriy"),
    )

    NOUN_MAKING = (
        ("morfologik", "Morfologik usul"),
        ("sintaktik", "Sintaktik usul"),
    )

    word = models.CharField(max_length=100)
    noun_types = models.CharField(max_length=15, choices=NOUN_TYPES, default=NOUN_TYPES[0][0])
    noun_types_structure = models.CharField(max_length=15, choices=NOUN_TYPES_STRUCTURE, default=NOUN_TYPES_STRUCTURE[0][0])
    noun_making = models.CharField(max_length=15, choices=NOUN_MAKING, default=NOUN_MAKING[0][0])
    review = models.CharField(max_length=1000)
    synonym = models.ManyToManyField(Synonym, blank=True)
    antonym = models.ManyToManyField(Antonym, blank=True)
    hyponym = models.ManyToManyField(Hyponym, blank=True)
    hyperonym = models.ManyToManyField(Hyperonym, blank=True)