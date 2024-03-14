export PYTHONPATH=$PWD/:$PYTHONPATH
python custom_infer/generate_prob.py --cfg configs/X3D_L.yaml NUM_GPUS 1 TRAIN.ENABLE False DATA.PATH_TO_DATA_DIR A2
python custom_infer/infer_result.py --cfg configs/X3D_L.yaml NUM_GPUS 1 TRAIN.ENABLE False DATA.PATH_TO_DATA_DIR A2
