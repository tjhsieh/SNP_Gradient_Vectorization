#!/bin/bash

for n in {60..99}
do
    file="../data/single_strokes/sunflowers_rendered_single_stroke_00$n.png"
    python main.py --config config/base.yaml --experiment experiment_5x1 --signature sunflowers --target $file --log_dir log/

done