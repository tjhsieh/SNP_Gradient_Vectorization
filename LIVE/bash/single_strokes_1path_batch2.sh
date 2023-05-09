#!/bin/bash
for n in {2..9}
do
    file="data/single_strokes/sunflowers_rendered_single_stroke_000$n.png"
    python main.py --config config/base.yaml --experiment experiment_1x1 --signature sunflowers --target $file --log_dir log/test

done

for n in {10..99}
do
    file="data/single_strokes/sunflowers_rendered_single_stroke_00$n.png"
    python main.py --config config/base.yaml --experiment experiment_1x1 --signature sunflowers --target $file --log_dir log/test

done

for n in {100..199}
do
    file="data/single_strokes/sunflowers_rendered_single_stroke_0$n.png"
    python main.py --config config/base.yaml --experiment experiment_1x1 --signature sunflowers --target $file --log_dir log/test

done

for n in {451..495}
do
    file="data/single_strokes/sunflowers_rendered_single_stroke_0$n.png"
    python main.py --config config/base.yaml --experiment experiment_1x1 --signature sunflowers --target $file --log_dir log/test

done
