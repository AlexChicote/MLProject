from src.mlProject.utils import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from mlProject.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline 


logger.info("Welcome to our custom logging")

STAGE_NAME="Data Ingestion Stage"
try:
    logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion= DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Stage"

try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<")
        data_validation = DataValidationTrainingPipeline()
        data_validation.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = DataTransformationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Model Trainer Stage'

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<<")
    obj = ModelTrainerTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>>>stage{STAGE_NAME} started <<<<<<<<")
    obj = ModelEvaluationTrainingPipeline()
    obj.main()
    logger.info(f">>>>>>>>stage {STAGE_NAME} comp[leted <<<<<<<<<<<<\n\nx=============x]")
except Exception as e:
    raise e
