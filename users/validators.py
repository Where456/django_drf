from rest_framework.exceptions import ValidationError


class PayValidator:
    """ Класс валидатора, который проверяет, что оплачиваться будет курс или урок """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        pay_value1 = dict(value).get(self.field1)
        pay_value2 = dict(value).get(self.field2)

        if (pay_value1 is None and pay_value2 is None) or (pay_value1 is not None and pay_value2 is not None):
            raise ValidationError('Можно оплатить или курс, или урок')