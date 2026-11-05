# Predicting Prolonged Hospital Length of Stay Using ICU Patient Data

**Author:** Ruiyang Hu | **BIOSTAT 707 Final Project - Individual Project**  
**Selected topic:** Project #1: Prolonged Length of Stay (Easier)

## Background and Research Question

Prolonged hospitalization after ICU admission can complicate resource planning. This project aims to determine whether information collected during the first 48 hours of ICU admission can predict hospital length of stay >14 days among hospital survivors. Because early death can shorten observed stays, a sensitivity analysis will examine in-hospital death or prolonged stay.

## Data Source and License

The analysis will use only Set A of the [PhysioNet/CinC Challenge 2012, version 1.0.0](https://physionet.org/content/challenge-2012/1.0.0/): `set-a.zip` and `Outcomes-a.txt`. These public data carry the Open Data Commons Attribution License v1.0 (ODC-BY). The requested Challenge citation is Silva I, Moody G, Scott DJ, Celi LA, Mark RG (2012), "Predicting in-hospital mortality of patients in ICU: The PhysioNet/Computing in Cardiology Challenge 2012," *Computing in Cardiology*, 39:245-248 ([article](https://pmc.ncbi.nlm.nih.gov/articles/PMC3965265/)). Raw data will remain local; `src/download_data.py` provides reproducible downloading and extraction.

## Study Population and Outcome Definition

The source describes adult ICU stays of at least 48 hours. Completed notebook inspection identified 4,000 patient files and 4,000 unique outcome records, with no duplicate or unmatched identifiers. Sixty records had missing length of stay; all death indicators were valid. Requiring a matched file, nonmissing nonnegative length of stay, and binary death status yielded 3,940 eligible stays.

The primary population comprised 3,386 survivors, including 1,025 (30.3%) with stays >14 days. The primary analysis will retain this definition; exactly 14 days will count as negative. Excluding deaths avoids treating early death as a favorable short stay but conditions the analysis on eventual survival. The sensitivity analysis will use all 3,940 eligible stays and define an event as in-hospital death or stay >14 days; inspection identified 1,579 events (40.1%). The same missing-outcome exclusions will apply.

Prediction will occur 48 hours after ICU admission. The documented length-of-stay variable measures days from ICU admission to the end of hospitalization, including time after ICU discharge, rather than ICU duration or time before ICU admission. The target will be this recorded duration, not remaining days after prediction. Local inspection identified one survivor record with length of stay of one day, inconsistent with the documented minimum ICU duration. Its timing will be reviewed before modeling, and any additional exclusions will be reported; counts above reflect the completed notebook definition.

## Predictor Variables

Predictors will include admission age, recorded sex, ICU type, height, and weight; vital signs; laboratory measurements; Glasgow Coma Scale; urine output; and mechanical ventilation. Repeated numeric values will be summarized by their median over 00:00-48:00, urine output by its recorded sum, and ventilation by any recorded use. Absent ventilation records will remain missing. RecordID and all outcome-table variables, including SAPS-I and SOFA, will be excluded.

Local inspection using the notebook's availability rules found no valid troponin I or T measurements among primary survivors; cholesterol was unavailable for 92.4%. These describe absence of any valid first-48-hour measurement per stay. Invalid measurements and source missing-value codes will become missing under documented rules. Feature construction will remain limited to these simple summaries.

## Planned Statistical and Machine Learning Methods

Three classifiers will be compared: unpenalized logistic regression using age, recorded sex, and ICU type as a simple baseline; ridge logistic regression with expanded predictors; and random forest with the same expanded predictors. Numeric missing values will receive training-sample medians; categorical missing values will receive an unknown category. Categorical variables will be encoded, and numeric variables will be standardized for logistic regression. Features entirely missing in a training fold will be omitted within that fold. All learned preprocessing will be fitted within training folds. Small tuning grids will vary ridge penalty strength and forest depth and minimum leaf size. No models have been trained; aggregation and imputation remain planned work.

## Validation and Model Evaluation

Each endpoint will use a reproducible, outcome-stratified 80% training/20% test split by ICU stay and five-fold stratified cross-validation within training data. Settings will be selected by cross-validated AUROC. Test data will be reserved for final evaluation without further tuning. Evaluation will include AUROC, Brier score, calibration plots, and calibration intercepts and slopes. Constant training-prevalence predictions will contextualize Brier scores.

Standardized logistic coefficients and random-forest permutation importance will describe predictive associations, with correlated variables interpreted cautiously. The endpoint analyses will compare prevalence, discrimination, calibration, and predictor rankings under the same feature rules and model classes. Differences will reflect changes in both population and endpoint, rather than improvement on an identical prediction task.

## Expected Findings

Markers of illness severity and organ dysfunction may help predict prolonged hospitalization, while including deaths may change predictor rankings. The analysis will test whether expanded models improve on the baseline and whether discrimination gains accompany adequate calibration. These are hypotheses; no model performance or superiority has been established.

## Limitations

Conditioning on eventual survival will limit application of the primary model to unselected patients at 48 hours. The composite will combine distinct clinical events. Irregular and missing measurements may reflect care practices; median imputation will not resolve informative missingness. Timing inconsistencies and implausible values require review. RecordID identifies stays rather than people, preventing reliable grouping of repeated admissions and potentially compromising split independence. Set A will provide internal validation only, with uncertain transportability to contemporary practice. Predictor importance will describe associations rather than causal effects.
