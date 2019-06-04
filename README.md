# Physics Ph.D. Admissions

I analyzed data from [TheGradCafe](https://www.thegradcafe.com/), a website that allows users to post admissions results, in order to see if I can predict Physics Ph.D. Admissions based on students Grades and GRE scores.

The data was scraped by Github user [evansjames](https://github.com/evansrjames/) and freely available [here](https://github.com/evansrjames/gradcafe-admissions-data). After downloading the CSV file containing the physics admissions results, I cleaned the data by dropping NaNs, filtering out erroneous data, one-hot-encoding some categorical features, and selecting on Ph.D. admissions only. 

From there, a quick exploratory data analysis quickly revealed the data to be largely non-separable. In order to potentially increase the separability, I perform some feature transformations. Through trial-and-error, I selected for the best features by only keeping features that improve the roc_auc_scores.

Afterward, I compare the following models to see which performs best. In order from best-to-worst, the models I tried are: random forest, xgboost, decision tree, svc, logistic regression, and Gaussian naive bayes.  Since random forest performed the best, I used a tuning grid in order to limit the tree depth and number of trees to improve model speed.

Finally, I use random forest with untransformed features to derive the relative importance as a sanity check.