from models.individual import Individual


def test_individual_age():
    person = Individual(
        "101",
        "John",
        "Addr",
        "999",
        "a@b.com",
        "pass",
        "Doe",
        "M",
        2000,
    )

    age = person.work_out_age()
    assert age > 0