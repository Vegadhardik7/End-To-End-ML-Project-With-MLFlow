import pandas as pd
import numpy as np  # kept for any downstream use
import joblib
import mlflow
from pathlib import Path
from urllib.parse import urlparse
from mlproject.entity.config_entity import ModelEvaluationConfig

from sklearn.metrics import (
    accuracy_score,
    precision_recall_fscore_support,
    roc_auc_score,
)
from sklearn.preprocessing import label_binarize

from src.mlproject.utils.common import save_json


class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    # -----------------------------------------------------------
    # Metric calculation
    # -----------------------------------------------------------
    def eval_metrics(self, actual, pred, prob, class_labels):
        acc = accuracy_score(actual, pred)
        precision, recall, f1, _ = precision_recall_fscore_support(
            actual, pred, average="macro"
        )

        # Macro one‑vs‑rest ROC‑AUC
        actual_bin = label_binarize(actual, classes=class_labels)
        auc = roc_auc_score(actual_bin, prob, average="macro", multi_class="ovr")

        return {
            "accuracy": acc,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "roc_auc": auc,
        }

    # -----------------------------------------------------------
    # MLflow logging
    # -----------------------------------------------------------
    def log_into_mlflow(self):
        # 1. Load data and model
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop(columns=[self.config.target_column])
        test_y = test_data[self.config.target_column]

        # 2. Configure MLflow URI
        mlflow.set_tracking_uri(self.config.mlflow_uri)

        with mlflow.start_run():
            # 3. Predictions
            pred_y = model.predict(test_x)
            prob_y = model.predict_proba(test_x)

            # 4. Metrics
            class_labels = sorted(test_y.unique())
            scores = self.eval_metrics(test_y, pred_y, prob_y, class_labels)

            # Save metrics locally
            save_json(path=self.config.metric_file_name, data=scores)

            # Log params & metrics to MLflow
            mlflow.log_params(self.config.all_params)
            for key, val in scores.items():
                mlflow.log_metric(key, val)

            # 5. Log model artifact (✔ works on DagsHub / any backend)
            model_file = "model.pkl"
            joblib.dump(model, model_file)
            mlflow.log_artifact(model_file)
