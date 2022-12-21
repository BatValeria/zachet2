# from conf import MODEL


def main(pk_=1):
    while True:
        dict_ = {
            "model": "smt",
            "pk": pk_,
            "friends": {
                "title": "smt",
                "year": "smt",
                "pages": "smt",
                "isbn13": "smt",
                "rating": 5,
                "price": 123456.0,
                "author": [
                    "test_author_1",
                    "test_author_2"
                ]
            }
        }
        yield dict_
        pk_ += 1


if __name__ == "__main__":
    pk_ = main(5)

for _ in range(2):
    print(next(pk_))
