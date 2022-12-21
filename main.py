# from conf import MODEL


def main(pk_=1):
    while True:
        yield
        dict_ = {
            "model": "smt",
            "pk": "pk",
            "friends": {
                "title": "smt",
                "year": "smt",
                "pages": "smt",
                "isbn13": "smt",
                "rating": 5,
                "price": 123456.0,
                "author": [
                ]
            }

        }
    pk_ += 1


if __name__ == "__main__":
    pk_ = main(5)

for _ in range(1):
    print(next(main()))
