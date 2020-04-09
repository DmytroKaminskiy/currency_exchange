from django.db import models

from currency import model_choices as mch


class Rate(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    currency = models.PositiveSmallIntegerField(choices=mch.CURRENCY_CHOICES)
    buy = models.DecimalField(max_digits=4, decimal_places=2)
    sale = models.DecimalField(max_digits=4, decimal_places=2)
    source = models.PositiveSmallIntegerField(choices=mch.SOURCE_CHOICES)

    def __str__(self):
        return f'{self.created} {self.get_currency_display()} {self.buy} {self.sale}'

    def save(self, *args, **kwargs):
        from django.core.cache import cache

        if not self.id:
            from currency.utils import generate_rate_cache_key
            cache_key = generate_rate_cache_key(self.source, self.currency)
            cache.delete(cache_key)

        super().save(*args, **kwargs)

    @classmethod
    def create_random_rate(cls):
        import random
        cls.objects.create(
            currency=random.choice([1, 2]),
            buy=random.randint(20, 30),
            sale=random.randint(20, 30),
            source=random.choice([1, 2]),
        )
