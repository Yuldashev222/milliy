from django.db import models
from mainapp.models import Synonym, Antonym, Hyponym, Hyperonym


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

    word = models.CharField(verbose_name="So'z", max_length=100, unique=True)
    noun_types = models.CharField(verbose_name="Ot turi", max_length=15, choices=NOUN_TYPES, default=NOUN_TYPES[0][0])
    noun_types_structure = models.CharField(verbose_name="Tuzilishiga ko'ra turi", max_length=15, choices=NOUN_TYPES_STRUCTURE, default=NOUN_TYPES_STRUCTURE[0][0])
    noun_making = models.CharField(verbose_name="Ot yasalishiga ko'ra turi", max_length=15, choices=NOUN_MAKING, default=NOUN_MAKING[0][0])
    review = models.CharField(max_length=1000, blank=True)
    synonym = models.ManyToManyField(Synonym, related_name="qw", blank=True)
    antonym = models.ManyToManyField(Antonym, related_name="qwe", blank=True)
    hyponym = models.ManyToManyField(Hyponym, related_name="qwer", blank=True)
    hyperonym = models.ManyToManyField(Hyperonym, related_name="qwerty", blank=True)

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
