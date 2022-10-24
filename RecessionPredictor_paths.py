"""
This module contains objects (mainly filepaths) to be used by other modules.
"""
import os
import datetime as dt

from pathlib import Path

os.chdir(os.path.dirname(os.path.abspath(__file__)))


fred_api_key = "fadb89baf8c1a1649586e27bf2d99e0f"
now = dt.datetime.now()
month = now.strftime("%m")
year = now.year
sp500_precutoff_data = Path("data/raw/SP500_pre-cutoff_data.json")
data_primary = Path("data/raw/primary_dataset_v{}_{}_01.json".format(year, month))
data_primary_most_recent = Path("data/raw/primary_dataset_most_recent.json")
data_secondary = Path(
    "data/interim/secondary_dataset_v{}_{}_01.json".format(year, month)
)
data_secondary_most_recent = Path("data/interim/secondary_dataset_most_recent.json")
data_final = Path("data/processed/final_dataset.json")
exploratory_plots = Path("reports/figures/exploratory.pdf")
test_results_plots = Path("reports/figures/test_results.pdf")
deployment_results_plots = Path("reports/figures/deployment_results.pdf")
cv_results = Path("models/model_metadata/cv_results.json")
cv_metadata = Path("models/model_metadata/cv_metadata.json")
pred_model_metadata = Path("models/model_metadata/pred_metadata.json")
prediction_errors = Path("models/model_metadata/prediction_errors.json")
full_predictions = Path("models/model_metadata/full_predictions.json")
knn_test_results = Path("models/testing_data/knn_test_results.json")
elastic_net_test_results = Path("models/testing_data/elastic_net_test_results.json")
naive_bayes_test_results = Path("models/testing_data/naive_bayes_test_results.json")
svm_test_results = Path("models/testing_data/svm_test_results.json")
gauss_test_results = Path("models/testing_data/gauss_test_results.json")
xgboost_test_results = Path("models/testing_data/xgboost_test_results.json")
weighted_average_test_results = Path(
    "models/testing_data/weighted_average_test_results.json"
)
deployment_cv_results = Path("models/model_metadata/deployment_cv_results.json")
deployment_cv_metadata = Path("models/model_metadata/deployment_cv_metadata.json")
deployment_pred_model_metadata = Path(
    "models/model_metadata/deployment_pred_metadata.json"
)
deployment_full_predictions = Path(
    "models/model_metadata/deployment_full_predictions.json"
)
deployment_svm_test_results = Path(
    "models/testing_data/deployment_svm_test_results.json"
)
deployment_chart_data = Path("reports/deployment_chart.csv")

# MIT License
#
# Copyright (c) 2019 Terrence Zhang
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
