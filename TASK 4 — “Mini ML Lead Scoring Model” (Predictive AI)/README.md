# Mini ML Lead Scoring Model (Predictive AI)

This project implements a predictive lead scoring model using machine learning.

* **Task:** “Mini ML Lead Scoring Model” (Predictive AI)

* **Environment:** All steps are implemented and documented in the provided Jupyter notebook, including:

  * Generating synthetic dataset with features such as:

    * `company_size`
    * `industry`
    * `tech_stack_keywords`
    * `page_visits`
    * `intent_signal`
    * `historical_conversion_rate`
    * `converted` (0/1)
  * Model training using XGBoost
  * Evaluation report including classification metrics and confusion matrix
  * Feature importance analysis
  * Distribution of lead scores (Bonus) is also provided with visualization. In fact, all the evaluation methods are visualized.

* **Requirements:** See `requirements.txt` for the list of dependencies.

* **Author:** Mubdiul Hossain

---

#### Recommendations for next improvements

* Tune hyperparameters (learning rate, depth, estimators).
* Try better categorical encoding (target encoding, CatBoost).
* Add feature engineering (interactions, better text/keyword encoding).
* Address class imbalance (already implemented)
* Calibrate probabilities for more reliable lead scores.
