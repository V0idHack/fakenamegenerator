from flask import Flask, render_template
from faker import Faker

app = Flask(__name__)

# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', 
# '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__',
#  '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__',
#  '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', 
# '__subclasshook__', '__weakref__', '_factories', '_factory_map', '_locales', 
# '_map_provider_method', '_select_factory', '_weights', 'add_provider', 'address',
#  'am_pm', 'android_platform_token', 'ascii_company_email', 'ascii_email', 
# 'ascii_free_email', 'ascii_safe_email', 'bank_country', 'bban', 'binary', 
# 'boolean', 'bothify', 'bs', 'building_number', 'cache_pattern', 'catch_phrase', 
# 'century', 'chrome', 'city', 'city_prefix', 'city_suffix', 'color', 'color_name', 
# 'company', 'company_email', 'company_suffix', 'coordinate', 'country', 'country_calling_code',
#  'country_code', 'credit_card_expire', 'credit_card_full', 'credit_card_number', 
# 'credit_card_provider', 'credit_card_security_code', 'cryptocurrency', 
# 'cryptocurrency_code', 'cryptocurrency_name', 'csv', 'currency', 'currency_code', 
# 'currency_name', 'currency_symbol', 'date', 'date_between', 'date_between_dates', 
# 'date_object', 'date_of_birth', 'date_this_century', 'date_this_decade', 
# 'date_this_month', 'date_this_year', 'date_time', 'date_time_ad', 'date_time_between', 
# 'date_time_between_dates', 'date_time_this_century', 'date_time_this_decade', 
# 'date_time_this_month', 'date_time_this_year', 'day_of_month', 'day_of_week', 
# 'dga', 'domain_name', 'domain_word', 'dsv', 'ean', 'ean13', 'ean8', 'ein', 
# 'email', 'factories', 'file_extension', 'file_name', 'file_path', 'firefox', 
# 'first_name', 'first_name_female', 'first_name_male', 'format', 'free_email',
#  'free_email_domain', 'future_date', 'future_datetime', 'generator_attrs', 
# 'get_formatter', 'get_providers', 'hex_color', 'hexify', 'hostname', 'http_method', 
# 'iban', 'image_url', 'internet_explorer', 'invalid_ssn', 'ios_platform_token', 
# 'ipv4', 'ipv4_network_class', 'ipv4_private', 'ipv4_public', 'ipv6', 'isbn10', 
# 'isbn13', 'iso8601', 'items', 'itin', 'job', 'language_code', 'language_name', 
# 'last_name', 'last_name_female', 'last_name_male', 'latitude', 'latlng', 'lexify',
#  'license_plate', 'linux_platform_token', 'linux_processor', 'local_latlng', 'locale', 
# 'locales', 'localized_ean', 'localized_ean13', 'localized_ean8', 'location_on_land', 
# 'longitude', 'mac_address', 'mac_platform_token', 'mac_processor', 'md5', 'military_apo', 
# 'military_dpo', 'military_ship', 'military_state', 'mime_type', 'month', 'month_name',
#  'msisdn', 'name', 'name_female', 'name_male', 'null_boolean', 'numerify', 'opera', 
# 'paragraph', 'paragraphs', 'parse', 'password', 'past_date', 'past_datetime', 
# 'phone_number', 'port_number', 'postalcode', 'postalcode_in_state', 
# 'postalcode_plus4', 'postcode', 
# 'postcode_in_state', 'prefix', 'prefix_female', 'prefix_male', 'profile', 
# 'provider', 'providers', 'psv', 'pybool', 'pydecimal', 'pydict', 'pyfloat', 
# 'pyint', 'pyiterable', 'pylist', 'pyset', 'pystr', 'pystr_format', 'pystruct', 
# 'pytimezone', 'pytuple', 'random', 'random_choices', 'random_digit', 
# 'random_digit_not_null', 'random_digit_not_null_or_empty', 'random_digit_or_empty',
#  'random_element', 'random_elements', 'random_int', 'random_letter', 'random_letters', 
#  'random_lowercase_letter', 'random_number', 'random_sample', 'random_uppercase_letter', 
#  'randomize_nb_elements', 'rgb_color', 'rgb_css_color', 'safari', 'safe_color_name', 'safe_email', 
#  'safe_hex_color', 'secondary_address', 'seed', 'seed_instance', 'seed_locale', 'sentence',
#   'sentences', 'set_formatter', 'sha1', 'sha256', 'simple_profile', 'slug', 'ssn', 'state',
#    'state_abbr', 'street_address', 'street_name', 'street_suffix', 'suffix', 'suffix_female',
#     'suffix_male', 'tar', 'text', 'texts', 'time', 'time_delta', 'time_object', 'time_series', 
#     'timezone', 'tld', 'tsv', 'unix_device', 'unix_partition', 'unix_time', 'upc_a', 'upc_e', 'uri', 
#     'uri_extension', 'uri_page', 'uri_path', 'url', 'user_agent', 'user_name', 'uuid4', 'weights', 
#     'windows_platform_token', 'word', 'words', 'year', 'zip', 'zipcode', 'zipcode_in_state', 'zipcode_plus4']

@app.route('/')
def index():
    locals = ['American', 'American', 'Arabic', 'Croatian', 'Czech', 'Dutch', 'Finnish', 'French', 'German',
                      'Hungarian', 'Italian', 'Japanese', 'Norwegian', 'Polish', 'Russian', 'Slovenian', 'Swedish', 'Thai']
    faker = Faker(locals)
    return render_template('index.jinja2', faker=faker)



if __name__ == '__main__':
    app.run(debug=True)