from django.contrib.auth import get_user_model
from django.db.models import QuerySet

User = get_user_model()


class PostQuerySet(QuerySet):
    def get_by_author(self, user: User) -> QuerySet:
        return self.filter(author=user)
