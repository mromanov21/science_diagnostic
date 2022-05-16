from django.db import models

from .utils.coding import (
    answer_choices,
    children_choices,
    living_choices,
    martial_status_choices,
    sex_choices,
    work_status_choices,
    yes_no_choices,
)

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField(verbose_name="ID")
    time_create = models.DateTimeField(verbose_name="Время создания")
    time_changed = models.DateTimeField(verbose_name="Время изменения")
    name = models.CharField(max_length=150, verbose_name="Фамилия, Имя, Отчество")
    group = models.CharField(max_length=50, verbose_name="Группа")
    member_gz_2021_2022 = models.CharField(
        choices=yes_no_choices,
        max_length=10,
        null=True,
        blank=True,
        verbose_name="Участник GZ 2021-2022",
    )
    sex = models.CharField(choices=sex_choices, max_length=50, verbose_name="Пол")
    age = models.CharField(max_length=30, verbose_name="Возраст")
    marital_status = models.CharField(
        choices=martial_status_choices, max_length=50, verbose_name="Семейное положение"
    )
    living = models.CharField(
        choices=living_choices, max_length=50, verbose_name="Проживаю"
    )
    children = models.CharField(
        choices=children_choices, max_length=40, verbose_name="Дети"
    )
    work_status = models.CharField(
        choices=work_status_choices, max_length=50, verbose_name="Занятость"
    )
    working_in_fishing_or_shipping = models.CharField(
        choices=yes_no_choices,
        null=True,
        max_length=30,
        verbose_name="Связана ли Ваша основная деятельность с рыбной отраслью и (или) мореходной деятельностью",
    )
    working_maritime = models.CharField(
        choices=yes_no_choices,
        null=True,
        max_length=30,
        verbose_name="морские профессии (судовождение, эксплуатация судовых энергетических установок)",
    )
    working_fishing_industry = models.CharField(
        choices=yes_no_choices,
        null=True,
        max_length=30,
        verbose_name="промышленное рыболовство",
    )
    working_fishing_technology = models.CharField(
        choices=yes_no_choices,
        max_length=30,
        null=True,
        verbose_name="технология рыбы и рыбных продуктов, морская биотехнология",
    )
    working_aquaculture = models.CharField(
        choices=yes_no_choices,
        max_length=30,
        null=True,
        verbose_name="аквакультура и рыбоводство",
    )
    working_economic = models.CharField(
        choices=yes_no_choices,
        max_length=30,
        null=True,
        verbose_name="экономика и управления морехозяйственной/рыбохозяйственной деятельностью",
    )
    working_it = models.CharField(
        choices=yes_no_choices,
        max_length=30,
        null=True,
        verbose_name="информационные технологии в морехозяйственной/рыбохозяйственной деятельности",
    )
    working_other = models.CharField(
        choices=yes_no_choices, max_length=30, null=True, verbose_name="другое"
    )

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Question(models.Model):
    text_question = models.TextField()

    def __str__(self):
        return self.text_question


class Answers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=50, blank=True, null=True)
    answer_bin = models.CharField(
        choices=answer_choices, max_length=50, blank=True, null=True
    )

    def __str__(self):
        return self.answer
