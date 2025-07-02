<h1>Enhanced Gradient Vectorization for Non-Photorealistic Rendering via Two-Stage K-Means Clustering</h1>
<h3>Official PyTorch implementation of the manuscript "Enhanced Gradient Vectorization for Non-Photorealistic Rendering via Two-Stage K-Means Clustering", submitted to The Visual Computer.<h3>
<hr>
<p>
This study addresses the challenge of preserving brush stroke structures and gradient color transitions in non-photorealistic rendering (NPR) through a novel gradient-aware SVG vectorization technique. Building upon the Stylized Neural Painting (SNP) model, our method isolates individual brush strokes and vectorizes them independently, incorporating gradient control points to simulate continuous tonal variations. Experimental results demonstrate a significant reduction in path complexity while preserving the stylistic integrity of brush strokes, enhancing visual fidelity, and improving output quality for stylized NPR applications. Here, we show that our approach outperforms existing techniques in maintaining gradient color transitions and stroke structure, offering a promising solution for scalable and editable NPR outputs.
</p>
<hr>
<img src="https://annaljs.github.io/PaperWeb/img/background.png">

<p>This repository contains a complete implementation of the training and inference pipeline described in our paper, developed using the PyTorch framework. In addition to the core codebase, we provide several demonstration scripts designed to facilitate the reproduction of the results reported in the paper. Furthermore, users can apply the pipeline to their own datasets by following the usage instructions provided below.</p>

The implementation of the PNR in our code is partially adapted from the project:
<ul>
	<li><a href="https://github.com/jiupinjia/stylized-neural-painting">Stylized Neural Painting</a></li>
	<li><a href="https://github.com/ma-xu/LIVE">LIVE- Towards Layer-wise Image Vectorization</a></li>
</ul>



<h3>To produce our results</h3>

<p>
Use Jupyter Notebook environment to open SNP/demo.jpynb
Use Jupyter Notebook environment to open LIVE/demo.jpynb

 demo.ipynb
</p>

<pre>
    git clone https://github.com/tjhsieh/SNP_Gradient_Vectorization.git  
    cd LIVE
    python main.py --config config/all.yaml --experiment experiment_8x1 --signature demo1 --target data/demo1.png
</pre>


<div>
  <video controls width="1080" class="img-responsive" src="https://annaljs.github.io/PaperWeb/video/all(字幕).mp4" alt="">
</div>


<h3>License</h3>

<p dir="auto"><a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" rel="nofollow"><img alt="Creative Commons License" src="https://camo.githubusercontent.com/62be294f71c9a1885f9cd8f54aa8b8bd42d432fd14b5393a8b25bcd1f34daa42/68747470733a2f2f692e6372656174697665636f6d6d6f6e732e6f72672f6c2f62792d6e632d73612f342e302f38387833312e706e67" data-canonical-src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" style="max-width: 100%;"></a><span>  The code is licensed under a <a href="http://creativecommons.org/licenses/by-nc-sa/4.0/" rel="nofollow">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.</p>


<div class="markdown-heading" dir="auto"><h2 tabindex="-1" class="heading-element" dir="auto">Citation</h2><a id="user-content-citation" class="anchor" aria-label="Permalink: Citation" href="#citation"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path d="m7.775 3.275 1.25-1.25a3.5 3.5 0 1 1 4.95 4.95l-2.5 2.5a3.5 3.5 0 0 1-4.95 0 .751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018 1.998 1.998 0 0 0 2.83 0l2.5-2.5a2.002 2.002 0 0 0-2.83-2.83l-1.25 1.25a.751.751 0 0 1-1.042-.018.751.751 0 0 1-.018-1.042Zm-4.69 9.64a1.998 1.998 0 0 0 2.83 0l1.25-1.25a.751.751 0 0 1 1.042.018.751.751 0 0 1 .018 1.042l-1.25 1.25a3.5 3.5 0 1 1-4.95-4.95l2.5-2.5a3.5 3.5 0 0 1 4.95 0 .751.751 0 0 1-.018 1.042.751.751 0 0 1-1.042.018 1.998 1.998 0 0 0-2.83 0l-2.5 2.5a1.998 1.998 0 0 0 0 2.83Z"></path></svg></a></div>

<p dir="auto">If you use our code for your research, please cite the following paper:</p>



<pre class="notranslate">
<code>
@article{hsieh2025,
    title={Enhanced Gradient Vectorization for Non-Photorealistic Rendering via Two-Stage K-Means Clustering},
    author={Tung-Ju Hsieh and Jia-Shuan Lin},
    journal = {The Visual Computer},
    year={2025},
    volume = {109},
    number = {9},
    pages = {xxx--xxx}
}
</code>
</pre>




