import random

from faker import Faker

fake = Faker()


def generator_name(*args):
    return fake.name()


def generate_text(*args):
    return fake.text()


def generate_job(*args):
    return fake.job()


def generate_email(*args):
    return fake.email()


def generator_domain(*args):
    return fake.domain_name()


def generator_company(*args):
    return fake.company()


def generator_address(*args):
    return fake.address()


def generator_date(*args):
    return fake.date()


def generator_phone_number(*args):
    return fake.phone_number()


def generator_number(*args):
    return random.randint(args[0] if args[0] is not None else 0, args[1] if args[1] is not None else 1)
