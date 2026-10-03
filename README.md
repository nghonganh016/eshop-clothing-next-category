# E-shop category switching prediction

Machine Learning project for predicting whether an online shopper will **stay in the current product category or switch to another category on their next click**.

The project uses clickstream data from the **E-shop Clothing 2008** dataset and focuses on understanding whether current browsing information and short-term browsing history can help identify category switching behavior.

## Project objective

An e-commerce website may want to know whether a user is likely to continue browsing products from the current category or move to another category.

This project formulates that behavior as a binary classification problem:

- `0 = Stay`: the next click belongs to the same product category.
- `1 = Switch`: the next click belongs to a different product category.

The main research question is:

> Can users' current and historical browsing behavior help predict whether they will switch to another product category on their next click?

Two sub-questions are investigated:

- **RQ1:** How well can current browsing information predict category switching?
- **RQ2:** Does adding browsing history improve switch prediction?

The model predicts switching **given that another click occurs in the session**. It does not predict whether the user will leave the website or end the session.

## Business motivation

The prediction can support category-level recommendation decisions.

If the probability of switching is low, the website may continue prioritizing products from the current category.

If the probability of switching is high, the website may consider exposing the user to products from other categories.

This project does **not** build a complete recommendation system. It does not determine:

- which category the user will switch to;
- which exact product should be recommended;
- whether the user will end the browsing session;
- whether a click will lead to a purchase.

## Dataset

The project uses the **E-shop Clothing 2008** clickstream dataset.

Each row represents a product click within a browsing session. Relevant variables include:

| Feature | Description |
| --- | --- |
| `session ID` | Browsing session identifier |
| `order` | Position of the click within a session |
| `page 1 (main category)` | Current product category |
| `page 2 (clothing model)` | Clothing model identifier |
| `colour` | Product colour |
| `location` | Product position on the webpage |
| `model photography` | Product photography style |
| `price` | Product price |
| `page` | Catalogue page number |

The original dataset contains four main product categories:

1. Trousers
2. Skirts
3. Blouses
4. Sale

Clicks are first sorted by `session ID` and `order` so that the browsing sequence of each session is preserved.

## Target construction

The next category within each session is created using the following logic:

```python
df["next_category"] = (
    df.groupby("session ID")["page 1 (main category)"]
      .shift(-1)
)
```

The binary target is then defined as:

```python
df["switch_category"] = (
    df["next_category"] != df["page 1 (main category)"]
).astype(int)
```

Therefore:

```text
Stay   = next category == current category
Switch = next category != current category
```

The final click of each session is removed because it has no next click and therefore no valid prediction target.

First clicks are retained whenever another click exists.

## Historical features

Three simple historical features are constructed using only information available before or at the current click.

### `prev_category`

Category viewed immediately before the current click.

```text
0   = no previous click
1–4 = previous category
```

### `same_category_prev`

Indicates whether the previous and current categories are the same.

```text
-1 = no previous click
 0 = previous category is different
 1 = previous category is the same
```

### `category_visit_count`

Number of previous visits to the current category within the same session.

This feature uses `cumcount()` so that future clicks are never included.

## Feature sets

Two feature sets are compared.

### Current

Uses only information available at the current click:

```text
page 1 (main category)
order
price
colour
location
model photography
page
```

### Current + History

Uses all Current features plus:

```text
prev_category
same_category_prev
category_visit_count
```

Comparing these two sets allows the project to test whether browsing history provides additional predictive value.

## Train/test strategy

The dataset is split into training and test sets using **session-level splitting**.

Approximately:

```text
80% sessions → training set
20% sessions → test set
```

All clicks from the same session must belong entirely to either the training set or the test set.

This avoids placing earlier clicks from a session in training and later clicks from the same session in testing.

The test set is kept unchanged across all models.

Target-focused exploratory analysis is performed on the training set so that patterns from the test set do not influence feature or modeling decisions.

## Exploratory data analysis

EDA focuses on questions directly related to category switching rather than plotting every available variable.

The notebook investigates:

1. Stay vs Switch target distribution
2. Switch rate by current category
3. Switch rate by browsing position
4. Switch rate by recent category consistency
5. Switch rate by previous visits to the current category
6. Previous-to-current category transition patterns
7. Product price and switching
8. Catalogue page and switching

These analyses are used to understand the prediction problem and interpret why selected features may contain useful information.

## Models

The project evaluates several classification approaches.

### Always-Stay baseline

Predicts every observation as `Stay`.

This baseline demonstrates why Accuracy alone is misleading for an imbalanced target: a model may achieve high Accuracy while detecting no Switch observations.

### Logistic Regression

Used as a linear baseline.

The project compares:

- standard Logistic Regression;
- Logistic Regression with `class_weight="balanced"`;
- balanced Logistic Regression using Current + History features.

This helps evaluate both class imbalance handling and the incremental value of browsing history.

### Decision Tree

Used to model nonlinear decision rules while maintaining interpretability.

A controlled tree depth is used so that important decision rules can still be inspected.

### Random Forest

Two directly comparable Random Forest models are trained:

```text
Random Forest + Current
Random Forest + Current + History
```

Both use the same model settings.

The only difference is the feature set, allowing a controlled evaluation of whether historical features improve prediction.

### Support Vector Machine

SVM is included as an additional classifier representing a different approach to constructing decision boundaries.

The initial experiment uses Current + History features with class balancing and appropriate feature scaling.

Because kernel SVM can become computationally expensive on large datasets, runtime and memory requirements are considered when selecting the final implementation.

## Model evaluation

Because `Switch = 1` is the minority and business-interest class, **Accuracy is not used as the primary evaluation metric**.

The main metric is:

```text
Switch F1
```

Additional metrics include:

- Switch Precision
- Switch Recall
- Macro F1
- ROC-AUC
- Accuracy

The final model is selected based primarily on its ability to detect Switch observations while maintaining a reasonable balance between Precision and Recall.

## Model tuning

Hyperparameter tuning is performed only for the most promising model rather than every model in the notebook.

The tuning objective is to improve **Switch F1** without adding unnecessary model complexity.

When cross-validation is used during tuning, session groups must be preserved so that clicks from the same session do not appear in different folds.

The test set is reserved for final evaluation after model selection and tuning.

## Final model analysis

The selected model is examined using:

- classification report;
- confusion matrix;
- Switch Precision, Recall and F1;
- feature importance when supported by the selected model.

The confusion matrix is also interpreted from a business perspective:

- **False Positive:** the model predicts Switch although the user actually stays in the current category.
- **False Negative:** the model predicts Stay although the user actually switches category.

Feature importance is treated as supporting interpretation rather than proof that a feature improves test performance.

The effect of historical browsing information is evaluated primarily through controlled Current vs Current + History comparisons.

## Project structure

```text
.
├── Group01_EShopClothing_SwitchPrediction.ipynb
├── e-shop clothing 2008.csv
├── e-shop clothing 2008 data description.txt
├── requirements.txt
├── TEAM_RESPONSIBILITIES.md
└── README.md
```

The exact notebook filename may include a version suffix during development. The final submitted notebook should use one consistent filename.

## Team responsibilities

The notebook is divided among three team members.

### Hồng Anh

Responsible for:

- project overview;
- data understanding;
- target construction;
- historical feature construction;
- train/test split;
- exploratory data analysis;
- feature-set preparation.

### Phương Anh

Responsible for:

- preprocessing;
- evaluation metrics;
- baseline model;
- Logistic Regression;
- Decision Tree;
- Random Forest;
- Support Vector Machine;
- model tuning.

### Phương Linh

Responsible for:

- model comparison;
- final model selection;
- classification report;
- confusion matrix;
- best-model analysis;
- research-question synthesis.

### Whole team

Responsible for:

- business interpretation;
- limitations;
- future work;
- final conclusion.

More detailed task ownership is documented in `TEAM_RESPONSIBILITIES.md`.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/nghonganh016/eshop-clothing-switch-category.git
cd eshop-clothing-switch-category
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start JupyterLab

```bash
jupyter lab
```

Open the project notebook and run the cells from top to bottom.

## Reproducibility

To reproduce the project correctly:

1. Keep `e-shop clothing 2008.csv` in the project root directory.
2. Install all dependencies from `requirements.txt`.
3. Run the notebook from the first cell to the last cell.
4. Do not manually change the train/test split.
5. Preserve `random_state=42` where specified.
6. Do not use information from the test set for feature selection or model tuning.
7. Keep sessions intact during train/test splitting and cross-validation.

## Current limitations

The project has several limitations:

- Switch observations are less common than Stay observations.
- The dataset contains limited user-specific preference information.
- There are no cart, purchase, rating or explicit-feedback signals.
- The binary target does not identify the destination category.
- The model does not predict session exit.
- Single-click sessions cannot produce a valid next-click target.
- The dataset was collected in 2008 and may not represent modern e-commerce behavior.

## Future work

Possible extensions include:

### Destination category prediction

After predicting that a user will switch, a second-stage model could predict the destination category:

```text
Will the user switch?
        ↓
       Yes
        ↓
Which category will they switch to?
```

### Product-level recommendation

A later system could rank individual clothing models within relevant categories.

This would require richer preference and interaction signals.

### Stay / Switch / Exit modeling

A future version could extend the binary target to explicitly distinguish:

```text
Stay
Switch
Exit
```

### Richer behavioral data

Additional signals such as dwell time, search queries, cart activity, purchase history and previous sessions could provide a stronger representation of user intent.

## Dataset reference

Variable definitions follow the accompanying `e-shop clothing 2008 data description.txt`.

> Łapczyński, M. and Białowąs, S. (2013). *Discovering Patterns of Users' Behaviour in an E-shop - Comparison of Consumer Buying Behaviours in Poland and Other European Countries*. Studia Ekonomiczne, 151, pp. 144–153.