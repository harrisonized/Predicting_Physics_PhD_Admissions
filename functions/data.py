import math
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix
from .formatting import title_to_snake_case

pd.set_option('mode.chained_assignment', None)


# Objects included in this file:
# numerical_features

# Functions included in this file:
# # preprocess
# # filter_df
# # transform_features
# # make_confusion_matrix


numerical_features = [
    'gpa', 'gre_verbal', 'gre_quantitative', 'gre_writing', 'gre_subject',
    'american', 'papers', 'research', 'decision',
    'gpa_rev', 'gre_verbal_rev', 'gre_quantitative_rev', 'gre_writing_rev', 'gre_subject_rev', 'decision_rev', 
    'gpa_log', 'gre_verbal_log', 'gre_quantitative_log', 'gre_writing_log', 'gre_subject_log', 
    'gpa_sq', 'gre_verbal_sq', 'gre_quantitative_sq', 'gre_writing_sq', 'gre_subject_sq',
    'gre_verbal_pctl', 'gre_quantitative_pctl', 'gre_writing_pctl', 'gre_subject_pctl', 
    'grev_x_greq', 'grev_x_gres', 'greq_x_gres', 'grev_x_greq_x_gres'
]


def preprocess(df):
    """
    """
    df.columns = [title_to_snake_case(x) for x in df.columns] # column_names

    # One-hot encoding
    df['american'] = df['student_classification'].replace('A', 1).replace(['U', 'I', 'O'], 0)
    df['papers'] = df['comments'].str.contains(r'(?<!no) [Pp]ub|(?<!no) [Pp]aper', regex=True)
    df['papers'] = df['papers'].replace(True, 1).replace(False, 0).fillna(value=0)
    df['research'] = df['comments'].str.contains('(?<!no) [Rr]esearch', regex=True)
    df['research'] = df['research'].replace(True, 1).replace(False, 0).fillna(value=0)
    df['decision'] = df['accept_or_reject'].replace('Accepted', 1).replace(['Rejected', 'Wait listed', 'Other', 'Interview'], 0)

    # Clean
    df['gpa'] = df['gpa'].replace(' ', np.NaN)
    df['gpa'] = df['gpa'].apply(lambda x: float(x))
    
    return df


def filter_df(df):
    """
    """
    
    # Drop NaNs
    df = df.dropna(subset=['american'])
    df = df.dropna(subset=[
        'accept_or_reject', 'gpa', 'gre_verbal', 'gre_quantitative', 'gre_writing', 'gre_subject'
    ]).reset_index(drop=True)

    # Filters
    df = df[(df['gpa'] <= 4)]  # Filter GPA
    df = df[(df['gre_verbal'] >= 130) & (df['gre_verbal'] <= 170)]
    df = df[(df['gre_quantitative'] >= 130) & (df['gre_quantitative'] <= 170)]
    df = df[(df['gre_writing'] > 1) & (df['gre_writing'] <= 5)]
    df = df[(df['gre_subject'] >= 400)]
    
    return df


def transform_features(df):
    """ Add log and sqrt values
    """
    # add log values for ols linear regression
    df['log_star_ratings'] = df['star_ratings'].apply(lambda x: math.log(x+1, 10))
    df['log_ticks'] = df['ticks'].apply(lambda x: math.log(x+1, 10))
    df['log_avg_stars'] = df['avg_stars'].apply(lambda x: math.log(x+1, 10))
    df['log_length'] = df['length_'].apply(lambda x: math.log(x+1, 10))
    df['log_grade'] = df['grade'].apply(lambda x: math.log(x+2, 10))
    df['log_on_to_do_lists'] = df['on_to_do_lists'].apply(lambda x: math.log(x+1, 10)) # Target
    
    # add sqrt values for Poisson regression
    df['sqrt_star_ratings'] = df['star_ratings'].apply(lambda x: math.sqrt(x))
    df['sqrt_ticks'] = df['ticks'].apply(lambda x: math.sqrt(x))
    df['sqrt_avg_stars'] = df['avg_stars'].apply(lambda x: math.sqrt(x))
    df['sqrt_length'] = df['length_'].apply(lambda x: math.sqrt(x))
    df['sqrt_grade'] = df['grade'].apply(lambda x: math.sqrt(x+1))
    
    return df


def make_confusion_matrix(model, features, target, threshold=0.5):
    """Predict class 1 if probability of being in class 1 is greater than threshold
    """
    y_predict = (model.predict_proba(features)[:, 1] >= threshold)
    confusion = confusion_matrix(target, y_predict)
    return confusion
