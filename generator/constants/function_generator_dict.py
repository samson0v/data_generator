from generator.services.generator_data_functions import *

FUNCTIONS_DICT = {
    'TEXT': generate_text,
    'JOB': generate_job,
    'FULL_NAME': generator_name,
    'EMAIL': generate_email,
    'DOMAIN_NAME': generator_domain,
    'PHONE_NUMBER': generator_phone_number,
    'COMPANY_NAME': generator_company,
    'INTEGER': generator_number,
    'ADDRESS': generator_address,
    'DATE': generator_date
}
