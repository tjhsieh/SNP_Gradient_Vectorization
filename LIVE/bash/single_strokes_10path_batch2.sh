#!/bin/bash

for n in {168..199}
do
    file="data/single_strokes/single_strokes_495/sunflowers_rendered_single_stroke_0$n.png"
    python main.py --config config/base.yaml --experiment experiment_10x1 --signature sunflowers --target $file --log_dir log/test

done

for n in {451..495}
do
    file="data/single_strokes/single_strokes_495/sunflowers_rendered_single_stroke_0$n.png"
    python main.py --config config/base.yaml --experiment experiment_10x1 --signature sunflowers --target $file --log_dir log/test

done
