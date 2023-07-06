from tortoise import fields
from tortoise.models import Model


class AddBot(Model):
    id = fields.IntField(pk=True)
    user_id = fields.IntField(max_length=48, default=None)
    first_names = fields.CharField(max_length=48, default=None)
    usernames = fields.CharField(max_length=48, default=None)
    links = fields.CharField(max_length=100, default=None)

    class Meta:
        table = "add_links"

    def __str__(self):
        return f'{self.first_names} | {self.links}'



