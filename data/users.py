import dataclasses
import datetime


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    sex: str
    mobile_number: str
    birth_day: int
    birth_month: int
    birth_year: int
    subject: str
    hobbies: str
    picture: str
    address: str
    state: str
    city: str

    def full_date_of_birth(self):
        return datetime.datetime(self.birth_year, self.birth_month, self.birth_day)


Alexandra = User(
    first_name='Alexandra',
    last_name='Borland',
    email='borland3711@gmail.com',
    sex='Female',
    mobile_number='9992131512',
    birth_day=15,
    birth_month=6,
    birth_year=1998,
    subject='Maths',
    hobbies='Music',
    picture='img.png',
    address='Kondratyevsky prospect',
    state='Haryana',
    city='Karnal',
)


