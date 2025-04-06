import mlflow
from utils import read_yaml, mkdirs
from os.path import join, exists, dirname
from ultralytics import YOLO
from dotenv import load_dotenv
import dagshub

load_dotenv()
dagshub.init(repo_owner='3bdullah3yad', repo_name='SmartVision', mlflow=True)

model_path = join('app_temp', 'model', 'best.pt')

def fetch_model():
    if not exists(model_path):
        mkdirs([model_path])
        params = read_yaml("params.yaml")
        cfg = read_yaml("config.yaml")
        
        if params.inference.exp_name == 'from_cfg_train':
            experiment = dict(mlflow.get_experiment_by_name(cfg.train.exp_name))
        else:
            experiment = dict(mlflow.get_experiment_by_name(params.inference.exp_name))

        run_id = params.inference.run_id
        if run_id == 'latest':
            experiment_id = experiment['experiment_id']
            df = mlflow.search_runs([experiment_id], order_by=["end_time DESC"])
            run_id = df['run_id'][0]        

        mlflow.artifacts.download_artifacts(f'runs:/{run_id}/weights/best.pt', dst_path = dirname(model_path))

    return YOLO(model_path)