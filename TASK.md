# Project tasks

Status convention:

- [x] Completed
- [~] In progress
- [ ] Not started
- [!] Need review

## Current handoff status - 2026-09-29

- Notebook sections 1–11 are implemented, including raw EDA, all 11 history
  features, next_category, the fixed session split, and exports.
- Sections 12–18 now have specific implementation guidance and 16 comment-only
  TODO cells. Sections 19–21 have writing guidance. Guidance is not implementation.
- Phương Anh owns sections 12–13; Phương Linh owns 14–18; all members own 19–21.
- No model, imputation pipeline, or current-category reference rule is fitted yet.
- Keep 141,448 labeled rows; train 112,491 rows / 15,187 sessions; test 28,957
  rows / 3,797 sessions; no session overlap. Keep random_state=42.
- All existing code and outputs in sections 1–11 were preserved in this handoff.
- The preparation validator is now read-only and selects preparation cells by
  source rather than executing the EDA/model cells or overwriting saved outputs.
- Read SETUP_AND_COLLABORATION.md before editing. Finish shared preprocessing
  and training-only grouped validation before either member starts experiments.

## Phase 1 - Problem definition

[x] Understand dataset
[x] Define prediction task
[x] Define next_category target
[x] Define baseline vs proposed approach
[x] Define evaluation strategy

## Phase 2 - Data preparation

[x] Load dataset
[x] Inspect shape, columns and data types
[x] Check missing values
[x] Check duplicates
[ ] Validate categorical values against the data description
[x] Sort by session ID and order

## Phase 3 - Feature engineering

[x] Create previous-click features
[x] Create price-history features
[x] Create session-behavior features with strictly prior-click visit counts
[x] Create next_category
[x] Remove rows without next_category
[x] Check preparation-stage leakage: ordering, all historical features, targets,
    first occurrences, split integrity and predictor exclusions are asserted
[x] Document and preserve first-click structural missingness without imputation
[x] Define current and historical feature lists (exclude year and session ID)

## Phase 4 - Exploratory analysis

[x] Current and next-category distributions
[x] Conditional next-category tables with group counts
[x] Country, colour, location, photo view, price group, month, page, order, and products
[x] Numeric input correlation after history creation, with method and limitations
[ ] Optional session-length/repeat-click analysis only if it adds to the research question

Avoid unnecessary EDA.

## Phase 5 - Train/test preparation

[x] Create session_split in the notebook (80/20, random_state=42); verify that
    session memberships match the original train/test exports
[x] Assert no session overlap (verified result: 0)
[x] Regenerate train/test exports after visit-count correction and verify round trip
[ ] Define categorical features
[ ] Define numerical features
[ ] Build preprocessing pipeline
[ ] Handle first-click missing history using train-fitted preprocessing or explicit
    no-history conventions; fit encoders/scalers/imputers on training data only
[ ] Shared session-grouped validation inside training data; no test tuning
[x] Define and validate explicit predictor lists excluding year, session ID and
    next_category (exports retain these columns for traceability and labels)
[ ] Reuse the same session split for every model and E1-E4 comparison

## Phase 6 - Baseline experiments

[ ] Current-category reference rule on the fixed test rows

[ ] Logistic Regression
[ ] Decision Tree
[ ] Random Forest
[ ] XGBoost

Using Current Features only.

## Phase 7 - Proposed approach

[ ] Logistic Regression
[ ] Decision Tree
[ ] Random Forest
[ ] XGBoost

Using Current + Historical Features.

## Phase 8 - Model comparison

[ ] Accuracy comparison
[ ] Macro F1 comparison
[ ] Weighted F1 comparison
[ ] Confusion matrices
[ ] Select model for further analysis

## Phase 9 - Ablation study

[ ] E1 Current
[ ] E2 + Previous Click
[ ] E3 + Price History
[ ] E4 + Session Behavior

## Phase 10 - Interpretation

[ ] Feature importance
[ ] Behavioral interpretation
[ ] Business interpretation
[ ] Limitations

## Phase 11 - Final notebook cleanup

[ ] Check markdown
[ ] Check comments
[ ] Check charts
[ ] Remove redundant cells
[ ] Restart and run all
[ ] Verify notebook runs from top to bottom
