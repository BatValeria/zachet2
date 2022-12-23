# from conf import MODEL
import random
import json
from title import title_
from faker import Faker

fake = Faker()


def main(pk_=1):
    while True:
        dict_ = {
            "model": "smt",
            "pk": pk_,
            "fields": {
                "title": title_(),
                "year": random.randint(1870, 2022),
                "pages": random.randint(50, 1000),
                "isbn13": fake.isbn13(),
                "rating": round(random.uniform(1, 5), 1),
                "price": round(random.uniform(100, 5000), 2),
                "author": [
                    fake.name(),
                    fake.name()
                ]
            }
        }
        yield dict_
        pk_ += 1


if __name__ == "__main__":
    pk_ = main(5)

for _ in range(1):
    print(next(pk_))
