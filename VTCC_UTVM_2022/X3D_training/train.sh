export PYTHONPATH=$PWD/:$PYTHONPATH
python tools/run_net.py --cfg configs/X3D_L.yaml NUM_GPUS 1 DATA.PATH_TO_DATA_DIR data
