## From Syllabus

Research Paper. A research paper at least ten typed pages in length (1.5-spaced, not including bibliography) will be prepared describing original research or analysis conducted for this class.  Research conducted for another class, for pay, or for a thesis may not be used for this paper.  However, an appropriate extension of that work may be satisfactory. Paper topics must be approved in advance by the instructor: I have a list of interesting phenomena that smart students should perform analysis on! The inclusion of some form of computer modeling in the research is strongly encouraged & essentially required for most topics. There will be two research papers. The first (midterm) will cover a pre-assigned topic for the class. The second (final) will be on a topic of the student’s choosing.
 
The research paper should be written in a format similar to those used in recognized biological engineering journals (Biotechnology & Bioengineering; Tissue Engineering; Metabolic Engineering; Biochemical Engineering Journal; ACS Biomaterials Science & Engineering). The paper should include a literature review describing previous work published on the topic and indicating why the paper's objective is an appropriate "next logical step" in extending the understanding of the topic area. The student's original work and results, which may include analysis and interpretation of published data, theoretical developments, or mathematical modeling, should then be presented. The results should be discussed, showing to what extent the paper’s objective was accomplished.  Finally, the conclusions of the study should be given.  Additional material should be placed in appendices following the main body of the paper.  Please note that this assignment is not meant to be a literature review or a summary of one or more existing research paper(s). Original work, such as mathematical modeling or analysis of published data, is required. 

## Abstract Feedback (PS11 / PS12)

- Project is in scope
- I’m surprised that there is no comparable model that exists which relates the ApoE copy number with ER trafficking. 
- I’ll be looking for what is new in this model compared with existing literature, so incorporating previous modeling efforts and why your model can ask new questions. 
- The ODE framework is fine, with the following qualifications:
- I’m surprised that you are not incorporating gene synthesis (transcription) and translation rates into your model; these have the advantage of being measurable values, and I’d be surprised if there were no difference between isoform lengths. I’d definitely incorporate these factors in your model. 
- I remember a log - length (n) dependence, where your abstract figure shows a more linear - length (n) dependence. 
- For this simple ODE model, I will look closely at parameter sourcing particularly for the ERAD. Do we have evidence that there are differences in trafficking for these species, and do we have concrete parameter values for this compartmental model ? Bundling folding and processing may or may not be justified in this context.
- In the absence of this evidence, a potentially different project direction is using Bayesian analysis to infer these kinetic parameters given known ApoE-length (n) rates. 
- One of the problems with ERAD modeling in an ODE framework is that you will see in the older literature considerable stochastic effects. Some cells reach a threshold of misfolded protein and ERAD is overloaded, leading to absolutely no secretion. This may be too advanced for your model, but I’ll be looking for at the least a discussion of this limitation of your model with appropriate references in your results/discussion. 

## Proposed Abstract (PS10 / PS11)

Working Title: An Ordinary Differential Equations Framework for Lipoprotein(a) Expression Dynamics as a Function of Copy Number Variation Length 

Lipoprotein(a) [Lp(a)] is a highly atherogenic, prothrombotic, and proinflammatory lipoprotein with well-established causal associations with cardiovascular disease (CVD) risk. A defining feature of Lp(a) is the Kringle IV Type 2 (KIV-2) variable number tandem repeat (VNTR) region within the *LPA* gene, which encodes the apolipoprotein(a) [apo(a)] protein. KIV-2 copy number ranges from 1–40 repeats and accounts for 40–70% of variation in circulating Lp(a) concentrations, with shorter repeat lengths typically associated with higher endogenous Lp(a) concentrations. Despite >70% heritability and co-dominant structure, the mechanistic basis for this inverse relationship remains incompletely understood. The prevailing hypothesis implicates endoplasmic reticulum (ER) protein trafficking as the central regulatory bottleneck. Longer apo(a) isoforms require more extensive post-translational modification, before export, in turn, increasing exposure to ER-associated degradation (ERAD) machinery. This project develops an ordinary differential equation (ODE) model of apo(a) synthesis, folding, trafficking, and degradation as a function of KIV-2 repeat number. The model will incorporate: (1) isoform-length-dependent ER processing rates, (2) ERAD-mediated degradation as a function of ER processing time, and (3) secretion and hepatic assembly into Lp(a) particles. Expected results include steady-state apo(a) secretion curves as a function of repeat number that recapitulate the experimentally observed inverse relationship between KIV-2 copy number and Lp(a) concentration. Bifurcation and sensitivity analyses will identify rate-limiting steps in trafficking and degradation, with implications for therapeutic targeting of Lp(a) biosynthesis. Broadly, this framework may inform haplotype informed polygenic risk score construction for Lp(a)-associated CVD, supporting more equitable cardiovascular risk prediction across genetically diverse populations.



**Directly addressing professor feedback:**

~~1. **Sensitivity analysis / parameter tornado plot** — since they're specifically going to scrutinize your parameter sourcing, a panel showing how P_ss(n) changes when you perturb each parameter (lam, k_fold0, k_e, K_n_assem, etc.) by ±20% would preemptively address that concern. Could be a heatmap over (n, parameter) or a classic tornado chart at a fixed n.~~

2. **Transcription + translation rate breakdown** — the professor was surprised you didn't include these, and you *do* have k_tx(n) and k_tl(n) in your model. A figure explicitly showing M_ss(n), and how k_tx and k_tl individually scale with n, would show you incorporated the feedback and that these contribute to the overall inverse relationship.

3. **Exponential vs. MM ERAD comparison** — you already have `steady_state_mm` implemented. Plotting P_ss(n) under both ERAD models side-by-side would directly engage the "is bundling folding and ERAD justified?" question and also set up the stochastic limitations discussion.

**Other strong options:**

4. **Bayesian posterior panel** — you have pymc imported. If you run inference on lam (and maybe k_fold0) against the Rader 1994 data points, a posterior predictive plot with credible intervals would be visually compelling and directly address the professor's suggestion about Bayesian parameter inference.

5. **Rate-limiting step decomposition** — plot the flux through each step (transcription, translation, folding, ERAD, assembly) as a function of n. This makes the "rate-limiting step" narrative concrete and is a natural companion to the bifurcation/sensitivity aims you mentioned in the abstract.

6. **ERAD saturation / ER stress regime** — using your MM model, show what happens as you increase synthesis rate (or decrease K_M_ERAD) — the point where ERAD gets saturated and secretion collapses. This directly addresses the professor's comment about stochastic ERAD overload, framing it as a deterministic analog.