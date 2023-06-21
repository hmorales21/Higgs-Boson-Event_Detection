<h1>Higgs Boson Event Detection</h1>
<h2>Deep Learning Project</h2>
<hr>
<h2>Description:</h2>
<p>The LHC collides bunches of protons every 50 nanoseconds within each of its four experiments, each crossing producing a random number of proton-proton collisions (with a Poisson expectation between 10 and 35, depending on the LHC parameters) called events8. Two colliding protons produce a small firework in which part of the kinetic energy of the protons is converted into new particles. Most of the resulting particles are very unstable and decay quickly into a cascade of lighter particles.</p>
<p>Based on these properties, the properties of the decayed parent particle are inferred, and the inference chain is continued until reaching the heaviest primary particles. given the elusive nature of neutrinos, their minuscule mass, and the way they oscillate between flavors, one could very well imagine that the mass of leptons comes from an entirely different mechanism. Hence the importance of measuring as precisely as possible the coupling of the Higgs to tau arises.</p>
<p>Particle colliders enable us to probe the fundamental nature of matter by observing exotic particles produced by high-energy collisions. Because the experimental measurements from these collisions are necessarily incomplete and imprecise, machine learning algorithms play a major role in the analysis of experimental data. The high-energy physics community typically relies on standardized machine learning software packages for this analysis and devotes substantial effort towards improving statistical power by hand-crafting high-level features derived from the raw collider measurements. </p>

<h2>Problem Statement:</h2>
<p>With the given dataset we have to classify whether the given event was a signal or a background noise in the process of decay for Higgs particle acceleration.</p>

<p>Metric - <b>Precision</b></p>

<hr>
<h2>Project structure</h2>
<h3>Project 5</h3>
<ul>
    <li>assets</li>
        <p><a href="../assets/Dataset_Details.pdf">Dataset Details</a></p>
        <p><a href='"Searching for Higgs Boson Decay Modes with Deep Learning.pdf"'>Searching for Higgs Boson Decay Modes with Deep Learning.pdf</a></p>
    <li>datasets</li>
        <p>training.csv : original dataset</p>
        <p>training_post_EDA.csv : modified dataset after the EDA stage</p>
        <p>training_post_preprosessing.csv : modified dataset after the preprocessing stage</p>
    <li>notebooks</li>
        <p>1. hpa_classification_EDA.ipynb</p>
        <p>2. hpa_classification_Preprocessing.ipynb</p>
        <p>3. hpa_classification_modelling.ipynb</p>
        <p>3. hpa_classification_explainable.ipynb</p>
    <li>models</li>
        <p>model : </p>
    <li>deployment</li>
</ul>
<hr>
<p>Horacio Morales González<p>
<a href="https://twitter.com/LachoMorales"><img src="https://img.shields.io/twitter/follow/LachoMorales?style=social" alt="Twitter: LachoMorales"/></a>
<a href="https://www.linkedin.com/in/hmorales1970/"><img scr="https://img.shields.io/badge/-hmorales1970-blue?style=flat-square&logo=Linkedin&logoColor=white" alt="Linkedin: hmorales1970"/></a>
