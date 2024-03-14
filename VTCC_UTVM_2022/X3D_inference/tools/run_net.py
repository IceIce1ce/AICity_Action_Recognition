#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
"""Wrapper to train and test a video classification model."""
from slowfast.config.defaults import assert_and_infer_cfg
from slowfast.utils.misc import launch_job
from slowfast.utils.parser import load_config, parse_args
from train_net import train
import os

def main():
    """
    Main function to spawn the train and test process.
    """
    args = parse_args()
    cfg = load_config(args)
    cfg = assert_and_infer_cfg(cfg)
    for view in ["dashboard", "rearview", "right"]:
        for user_id in ["14786", "25077", "50347", "70176", "93439"]:
            cfg.view = view
            cfg.user_id = user_id
            cfg.OUTPUT_DIR = 'checkpoint_{}_{}'.format(view, user_id)
            if not os.path.exists(cfg.OUTPUT_DIR):
                os.makedirs(cfg.OUTPUT_DIR)
            # Perform training.
            if cfg.TRAIN.ENABLE:
                launch_job(cfg=cfg, init_method=args.init_method, func=train)

if __name__ == "__main__":
    main()