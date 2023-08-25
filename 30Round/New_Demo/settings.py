from os import environ

SESSION_CONFIGS = [
    dict(
        name='CBDC1_Jul20',
        app_sequence=['public_goods_simple', 'cbdc_instruc', 'quiz2', 'cbdc',
                      'six_player_instructions_cbdc', 'cbdc_extended', 'exit_survey_CB'],
        num_demo_participants=6,
    ),


    dict(
        name='CBDC2_Jul20',
        app_sequence=['public_goods_simple', 'cbdc_instruc', 'quiz2', 'cbdc',
                      'six_player_instructions_cbdc', 'cbdc_extended', 'exit_survey_CB'],
        num_demo_participants=6,
    ),


    dict(
        name='CBDC3_Jul20',
        app_sequence=['public_goods_simple', 'cbdc_instruc', 'quiz2', 'cbdc',
                      'six_player_instructions_cbdc', 'cbdc_extended', 'exit_survey_CB'],
        num_demo_participants=6,
    ),


]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """ """

SECRET_KEY = '4684667878377'
