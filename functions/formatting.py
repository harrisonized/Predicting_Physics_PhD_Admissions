import pandas as pd
pd.set_option('mode.chained_assignment', None)


# Objects included in this file:

# Functions included in this file:
# # title_to_snake_case


def title_to_snake_case(text):
    """Converts "Column Title" to column_title
    """
    return text.lower().replace(' ', '_').replace('-', '_')


def snake_to_title_case(text):
    """Converts column_title to "Column Title"
    """
    return ' '.join(map(lambda x: x.capitalize(), text.split('_')))
