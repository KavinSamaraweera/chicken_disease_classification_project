from src.cnnClassifier.config.configuration import ConfigurationManager
from src.cnnClassifier.components.prepare_callbacks import PrepareCallbacks
from src.cnnClassifier.components.training import Training
from src.cnnClassifier import logger

STAGE_NAME = "Training"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_callbacks_config = config.get_prepare_callbacks_config()
        prepare_callbacks = PrepareCallbacks(config=prepare_callbacks_config)
        callbacks_list = prepare_callbacks.get_tb_ckpt_callbacks()

        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()

        training.train(
            callback_list=callbacks_list
        )


#This is used to call dvc later
if __name__ == "__main__":

    try:
        logger.info(f"********")
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<< \n\nx========x")
    except Exception as e:
        logger.exception(e)
        raise e