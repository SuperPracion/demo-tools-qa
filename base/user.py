import settings
import dataclasses


@dataclasses.dataclass
class User:
    username: str = settings.DEFAULT_USERNAME
    password: str = settings.DEFAULT_PASSWORD

    def __str__(self):
        return f'{self.username} {self.password}'
