import math
import pandas as pd
import scipy.stats

pd.set_option('mode.chained_assignment', None)


# Objects included in this file:

# Functions included in this file:
# # add_rev
# # add_log
# # add_square
# # add_percentile
# # add_products


def add_rev(df):
    df['gpa_rev'] = df['gpa'].apply(lambda x: 4-x)
    df['gre_verbal_rev'] = df['gre_verbal'].apply(lambda x: 170-x)
    df['gre_quantitative_rev'] = df['gre_quantitative'].apply(lambda x: 170-x)
    df['gre_writing_rev'] = df['gre_writing'].apply(lambda x: 5-x)
    df['gre_subject_rev'] = df['gre_subject'].apply(lambda x: 990-x)
    df['decision_rev'] = df['decision'].apply(lambda x: 1-x)
    return df


def add_log(df):
    df['gpa_log'] = df['gpa_rev'].apply(lambda x:  math.log(x+1, 10))
    df['gre_verbal_log'] = df['gre_verbal_rev'].apply(lambda x: math.log(x+1, 10))
    df['gre_quantitative_log'] = df['gre_quantitative_rev'].apply(lambda x: math.log(x+1, 10))
    df['gre_writing_log'] = df['gre_writing_rev'].apply(lambda x: math.log(x+1, 10))
    df['gre_subject_log'] = df['gre_subject_rev'].apply(lambda x: math.log(x+1, 10))
    return df


def add_square(df):
    df['gpa_sq'] = df['gpa'].apply(lambda x: x**2)
    df['gre_verbal_sq'] = df['gre_verbal'].apply(lambda x: x**2)
    df['gre_quantitative_sq'] = df['gre_quantitative'].apply(lambda x: x**2)
    df['gre_writing_sq'] = df['gre_writing'].apply(lambda x: x**2)
    df['gre_subject_sq'] = df['gre_subject'].apply(lambda x: x**2)
    return df


def add_percentile(df):
    df['gre_verbal_pctl'] = df['gre_verbal'].apply(lambda x: scipy.stats.norm(150.05, 8.43).cdf(x))
    df['gre_quantitative_pctl'] = df['gre_quantitative'].apply(lambda x: scipy.stats.norm(152.80, 9.13).cdf(x))
    df['gre_writing_pctl'] = df['gre_writing'].apply(lambda x: scipy.stats.norm(3.5, 0.87).cdf(x))
    df['gre_subject_pctl'] = df['gre_subject'].apply(lambda x: scipy.stats.norm(712, 158).cdf(x))
    return df


def add_products(df):
    df['grev_x_greq'] = df['gre_verbal']**(0.5) * df['gre_quantitative']**(0.5)
    df['grev_x_gres'] = df['gre_verbal']**(0.5) * df['gre_subject']**(0.5)
    df['greq_x_gres'] = df['gre_quantitative']**(0.5) * df['gre_subject']**(0.5)
    df['grev_x_greq_x_gres'] = df['gre_verbal']**(1/3) * df['gre_quantitative']**(1/3) * df['gre_subject']**(1/3)
    return df
