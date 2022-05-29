from django.db import models


class Synonym(models.Model):
    word = models.CharField(verbose_name="so'z", max_length=100, unique=True)

    def __str__(self):
        return self.word


class Antonym(models.Model):
    word = models.CharField(verbose_name="so'z", max_length=100, unique=True)

    def __str__(self):
        return self.word


class Hyponym(models.Model):
    word = models.CharField(verbose_name="so'z", max_length=100, unique=True)

    def __str__(self):
        return self.word


class Hyperonym(models.Model):
    word = models.CharField(verbose_name="so'z", max_length=100, unique=True)

    def __str__(self):
        return self.word


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

    word = models.CharField(verbose_name="So'z", max_length=100, unique=True)
    adjectives_two = models.CharField(verbose_name="Belgi ifodalashiga ko‘ra turi", max_length=15, choices=ADJECTIVES_TYPES_TWO, default=ADJECTIVES_TYPES_TWO[0][0])
    adjective_type = models.CharField(verbose_name="Sifat turi", max_length=15, choices=ADJECTIVE_TYPES, default=ADJECTIVE_TYPES[0][0])
    adjective_level = models.CharField(verbose_name="Sifat darajasi", max_length=15, choices=ADJECTIVE_LEVELS, default=ADJECTIVE_LEVELS[0][0])
    adjective_type_structure = models.CharField(verbose_name="Tuzilish jihatdan turi", max_length=15, choices=ADJECTIVE_TYPE_STRUCTURE,
                                                default=ADJECTIVE_TYPE_STRUCTURE[0][0])
    review = models.CharField(verbose_name="Izoh", max_length=1000, blank=True)
    synonym = models.ManyToManyField(Synonym, verbose_name="Sinonim", related_name="synonyms", blank=True)
    antonym = models.ManyToManyField(Antonym, verbose_name="Antonim", blank=True)
    hyponym = models.ManyToManyField(Hyponym, verbose_name="Giponim", blank=True)
    hyperonym = models.ManyToManyField(Hyperonym, verbose_name="Giperonim", blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.word

    def get_synonyms(self):
        synonyms = []
        for obj in self.synonym.all():
            synonyms.append(obj.word)
        return synonyms

    def get_antonyms(self):
        antonyms = []
        for obj in self.antonym.all():
            antonyms.append(obj.word)
        return antonyms

    def get_hyponyms(self):
        hyponyms = []
        for obj in self.hyponym.all():
            hyponyms.append(obj.word)
        return hyponyms

    def get_hyperonyms(self):
        hyperonyms = []
        for obj in self.hyperonym.all():
            hyperonyms.append(obj.word)
        return hyperonyms


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
    noun_types_structure = models.CharField(max_length=15, choices=NOUN_TYPES_STRUCTURE,
                                            default=NOUN_TYPES_STRUCTURE[0][0])
    noun_making = models.CharField(max_length=15, choices=NOUN_MAKING, default=NOUN_MAKING[0][0])
    review = models.CharField(max_length=1000)
    synonym = models.ManyToManyField(Synonym, blank=True)
    antonym = models.ManyToManyField(Antonym, blank=True)
    hyponym = models.ManyToManyField(Hyponym, blank=True)
    hyperonym = models.ManyToManyField(Hyperonym, blank=True)
