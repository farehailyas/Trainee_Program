import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from statsmodels.tools.tools import add_constant
from scipy import stats

def get_data_frame():
    data = pd.read_csv("data/vehicle_price_prediction.csv")
    df = pd.DataFrame(data)
    return df

def visualize_numerical_features(df):
    cols = ['price', 'year', 'mileage', 'engine_hp', 'owner_count', 'vehicle_age', 'mileage_per_year', 'brand_popularity']
    sample = df[cols].sample(2000, random_state=42)
    sns.pairplot(data=sample)
    plt.savefig("relation_of_categories")

def calculate_vif_for_correlation(df):

    data = add_constant(df[['engine_hp' , 'mileage' , 'vehicle_age' , 'year' , 'mileage_per_year' ]])
    vif = pd.DataFrame()
    vif['Features'] = data.columns
    vif['variance_inflation_factor'] = [variance_inflation_factor(data.values, i ) for i in range(data.shape[1])]
    print(vif[vif['Features'] != 'const'])

def calculate_correlation(df):
    corr_age_mileage = df['vehicle_age'].corr(df['mileage'])
    print(f"correlation between age and mileage {corr_age_mileage}")  
    corr_year_mileage = df['year'].corr(df['mileage'])
    print(f"correlation between year and mileage {corr_year_mileage}") 

    corr_mileage_per_year_mileage = df['mileage_per_year'].corr(df['mileage'])
    print(f"correlation between mileage_per_year and mileage {corr_mileage_per_year_mileage}")  

    
    corr_price_mileage = df['price'].corr(df['mileage'])
    print(f"correlation between price and mileage {corr_price_mileage}")
    corr_price_engine = df['price'].corr(df['engine_hp'])
    print(f"correlation between price and engine {corr_price_engine}")


    corr_mileage_per_year_price = df['mileage_per_year'].corr(df['price'])
    print(f"correlation between mileage_per_year and price {corr_mileage_per_year_price}")  

def visualize_categorical_features(df):
    cols = ['body_type' , 'accident_history' , 'fuel_type' , 'condition' , 'transmission' , 'drivetrain' , 'seller_type', 'exterior_color' , 'interior_color' , 'trim']
    for col in cols:
        plt.figure(figsize=(10,6))
        sns.boxplot(data = df , x = col , y = 'price')
        plt.title(f"price by {col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig(f"price_by_{col}")
        plt.close()

def test_categorical_features(df):
    cols = ['body_type' , 'accident_history' , 'seller_type' , 'condition' , 'model' , 'make' ]
    overall_mean =  df['price'].mean()
    ss_total = ((df['price'] - overall_mean) ** 2).sum()

    res = pd.DataFrame()
    features , f_stats , p_values , eta_squares = [] , [] , [] , []

    for col in cols:
        categories = [grp['price'].values for i , grp in df.groupby(col)]
        f_stat , p_value = stats.f_oneway(*categories)
        grp1 = df.groupby(col)['price']
        ss_between = (grp1.count() * (grp1.mean() - overall_mean) ** 2).sum()
        eta_sq = ss_between / ss_total

        features.append(col)
        f_stats.append(f_stat)
        p_values.append(p_value)

        eta_squares.append(eta_sq)

    res['Feature'] = features
    res['F_statistic'] = f_stats
    res['p_value'] = p_values
    res['eta_squared'] = eta_squares
    print(res.sort_values('eta_squared', ascending=False))

df = get_data_frame()
"""visualize relation between numeric features and target variable price to find the trend"""
# visualize_numerical_features(df)

"""vehicle age and mileage have negative linear trend with price. engine_hp has psotive linear trend with price """
"""correlation found between mileage and vehicle age. find vif value for it"""
"""
Since mileage measures the real thing directly, and it's 0.78 correlated with age anyway, 
keeping mileage already captures most of what age would have told us â so we don't need age as a separate column.
Honest caveat (worth knowing)
It's not perfect â a 10-year-old car driven very little (say 30,000 miles) breaks the pattern. In those rare cases, mileage and age disagree. But for the 
vast majority of cars they line up, so mileage is a good enough single stand-in, and it avoids the redundancy problem of keeping both."""

calculate_vif_for_correlation(df)

calculate_correlation(df)

# visualize_categorical_features(df)
test_categorical_features(df)