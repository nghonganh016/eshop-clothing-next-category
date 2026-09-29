# Project context

## 1. Project objective

Dataset: E-shop clothing 2008.

Main task:
Predict the next product category that a user will click within the same session.

Target:
next_category

Classes:
- Trousers
- Skirts
- Blouses
- Sale

The target is constructed using:

df.groupby("session ID")["page 1 (main category)"].shift(-1)

This is NOT a purchase prediction problem because the dataset does not contain
Purchase, Checkout, or Revenue variables.

---

## 2. Main research question

Does historical browsing behavior within a session improve the prediction
of the user's next product category?

Main comparison:

Baseline:
Current click features only

vs.

Proposed approach:
Current click features + historical behavioral features

The comparison must use:
- the same train/test split
- the same models
- the same evaluation metrics

Primary metric:
Macro F1

Secondary metrics:
- Accuracy
- Weighted F1
- Confusion Matrix

---

## 3. Data splitting rule

DO NOT randomly split individual rows.

Train/test must be split by SESSION ID.

Approximately:
- 80% sessions for train
- 20% sessions for test

All rows from the same session must belong to the same split.

Reason:
prevent data leakage between train and test.

---

## 4. Feature groups

### Current features

- month
- day
- country
- order
- page 1 (main category)
- page 2 (clothing model)
- colour
- location
- model photography
- price
- price 2
- page

Do NOT use:
- year because it is constant at 2008
- session ID as a predictor

### Previous click features

- prev_category
- prev_product
- prev_location
- same_category_prev
- same_product_prev

### Price history features

- prev_price
- price_change
- avg_prev_price

### Session behavior features

- category_visit_count
- product_visit_count
- previous_clicks if used consistently

Important:
Historical features can only use information available BEFORE the current click.

Never use future clicks.

---

## 5. Required experiments

E1:
Current features only

E2:
Current + Previous Click

E3:
Current + Previous Click + Price History

E4:
    Current + Previous Click + Price History + Session Behavior

This is the ablation study.

Compare Macro F1 after each experiment.

---

## 6. Models

Required models:

1. Logistic Regression
2. Decision Tree
3. Random Forest
4. XGBoost

Each model must be evaluated with:

A. Current features only
B. Current + historical features

---

## 7. Evaluation

For every major model:

- Accuracy
- Macro F1
- Weighted F1

For selected/final models:

- Confusion Matrix
- classification report if useful

The main conclusion should answer:

"Does historical browsing behavior improve next-category prediction?"

Do NOT focus only on which model has the highest accuracy.

---

## 8. Notebook philosophy

The notebook should read like a complete data science project.

Every section should contain:

1. Purpose
2. Code
3. Result
4. Interpretation

Avoid code cells without explanation.

Avoid EDA charts that do not contribute to the modeling problem.

---

## 9. Business interpretation

The model may support:

- product recommendation
- website navigation
- promotion targeting

Do NOT claim that the model increases:

- purchases
- revenue
- conversion

because the dataset does not contain evidence for these outcomes.

---

## 10. Current project status

As of 2026-09-29, notebook sections 1–11 are implemented: data inspection, EDA,
session sorting, historical features, target creation, the session split, and CSV
exports. Keep the current completed code and outputs.

Sections 12–21 have task guidance, not completed modeling. Still to implement:
shared train-fitted preprocessing; session-grouped validation within training;
the current-category reference rule; all four models under E1 and E4; evaluation;
E1–E4 ablation; importance; interpretation; limitations; and conclusion.

Use the notebook's actual section numbers for handoff and
SETUP_AND_COLLABORATION.md for environment and Git instructions. The outline
below is the original conceptual outline, not a request to renumber the notebook.

---

## 11. Notebook structure
1. Project overview
   1.1 Background
   1.2 Research question
   1.3 Project contribution

2. Dataset understanding
   2.1 Dataset overview
   2.2 Feature description
   2.3 Target definition

3. Data quality assessment
   3.1 Missing values
   3.2 Duplicates
   3.3 Data types
   3.4 Data validity

4. Exploratory data analysis
   4.1 Target distribution
   4.2 Session characteristics
   4.3 Browsing behavior
   4.4 Category transitions

5. Feature engineering
   5.1 Session ordering
   5.2 Previous-click features
   5.3 Price-history features
   5.4 Session-behavior features
   5.5 Target creation

6. Train-test preparation
   6.1 Session-based split
   6.2 Leakage validation
   6.3 Preprocessing pipeline

7. Baseline modeling
   7.1 Logistic Regression
   7.2 Decision Tree
   7.3 Random Forest
   7.4 XGBoost

8. Historical behavior modeling
   8.1 Logistic Regression
   8.2 Decision Tree
   8.3 Random Forest
   8.4 XGBoost

9. Model comparison

10. Ablation study

11. Feature importance and interpretation

12. Business implications

13. Limitations

14. Conclusion