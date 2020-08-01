from django.db import models

DEFAULT_STATUS = 'active'

STATUS_CHOICE = [
    (DEFAULT_STATUS, 'Активно'),
    ('blocked', 'Заблокировано')
]


class Guestbook(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, verbose_name='Имя автора записи')
    email = models.EmailField(null=False, blank=False, verbose_name='Почта автора записи')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст записи')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания записи')
    redacted_date = models.DateTimeField(auto_now=True, verbose_name='Время последнего редактирования')
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, verbose_name='Статус')

    def __str__(self):
        return f'{self.pk}: {self.name} - {self.status}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
