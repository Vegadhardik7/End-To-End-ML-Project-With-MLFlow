from mlproject import logger
from mlproject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    dataingestion = DataIngestionTrainingPipeline()
    dataingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<<\n\n X==============X")
except Exception as e:
    logger.exception(e)
    raise e