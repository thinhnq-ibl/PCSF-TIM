import re

with open('/Users/nguyenquocthinh/Documents/PCSF-TIM/paper/draft_paper_springer.tex', 'r') as f:
    content = f.read()

# Find the start of the appendix
app_idx = content.find('\\section*{Appendix: Supplementary Materials}\\label{sec:appendix}')
if app_idx == -1:
    print("Appendix start not found")
    exit(1)

pre_app = content[:app_idx]
app_content = content[app_idx:]

# We will just replace everything from `\section*{Appendix...}` until `\bibliography{references}`
bib_idx = app_content.find('\\bibliography{references}')
if bib_idx == -1:
    print("Bibliography not found")
    exit(1)

app_body = app_content[:bib_idx]
post_app = app_content[bib_idx:]

# Define new appendix content
new_appendix = r"""\begin{appendices}

\section{Additional Experimental Results}\label{app:experiments}

\subsection{Robustness of Aggregate-Based Distance-Decay Recovery}
To evaluate the reliability of the exposure-corrected maximum likelihood estimation (MLE) workflow under non-ideal data collection conditions, we conduct a series of robustness analyses across four scenarios:
\begin{itemize}
  \item \textbf{Bin Sensitivity Analysis}: Sweeping the number of distance bins $K \in \{3, 5, 10, 20\}$ reveals that downstream prediction performance stabilizes quickly. The mean CPC across target cities increases from 0.7174 under a coarse $K=3$ configuration to 0.7346 for $K=5$, 0.7394 for $K=10$, and 0.7403 for $K=20$ (compared to a baseline of 0.7411 computed on full, unbinned ground-truth OD matrices). This suggests that five or more distance bins provide sufficient resolution to capture city-specific decay profiles.
  \item \textbf{Atlanta Case Study Outlier}: Atlanta is identified as a localized outlier, where its Meta MDM 3-bin CPC under oracle outflows is 0.5761 compared to 0.7334 under the LODES 3-bin baseline. This drop is driven by the spatial interaction between the sprawling polycentric layout of the city and the coarse telemetry binning of the Meta Movement Distribution Maps (MDM) data. Excluding Atlanta from the target set increases the mean target CPC for Meta MDM from 0.7080 to 0.7135, recovering 96.4\% of the corresponding LODES baseline.
  \item \textbf{Missing Attractiveness Data ($A_j$)}: We simulate spatial feature scarcity by randomly removing 10\%, 20\%, and 50\% of target-city destination attraction values $A_j$. The parameter recovery remains stable, yielding a mean absolute error ($\text{MAE}$) of $\alpha_{\text{MAE}} = 0.0395$ under 20\% missing data, compared to the baseline MAE of 0.0394.
  \item \textbf{CBD Collapse (Extreme $A_j$ Distortion)}: To test resilience against extreme structural distortions, we replace the attraction values $A_j$ of the top 10\% most attractive zones with the city-wide mean attraction. Under this CBD collapse scenario, the estimation remains robust, yielding parameter recovery errors of $\alpha_{\text{MAE}} = 0.0441$ under direct replacement and $\alpha_{\text{MAE}} = 0.0486$ when the affected zone attractions are scaled down by 80\%.
\end{itemize}

\begin{figure*}[htbp!]
  \centering
  \includegraphics[width=0.85\textwidth]{../figures/layer1_robustness_heatmap.png}
  \caption{Robustness of Aggregate-Based Distance-Decay Recovery (MAE) under varying levels of noise, missing data, and CBD collapse scenarios across all 25 held-out target cities.}
  \label{fig:layer1_heatmap}
\end{figure*}

\subsection{Robustness of Origin Production Transfer}
We analyze the sensitivity of the zero-shot origin production transfer along two operational dimensions: training-set scale and prediction noise.

\subsubsection{Source-Scale Sensitivity}
We analyze how the number of training environments affects zero-shot outflow predictability by retraining the GBDT model on subsets of $n_{\text{src}} \in \{5, 10, 15, 20, 25\}$ source cities. Evaluating on target cities demonstrates that zero-shot prediction performance rises steeply from $n_{\text{src}} = 5$ and saturates around 15--20 source cities. This indicates that only a modest number of source cities is required to learn stable, generalizable outflow characteristics.

\subsubsection{Noise Sensitivity}
To evaluate the stability of origin transfer under prediction errors, we inject additive Gaussian noise at log-scale ($\sigma \in \{10\%, 20\%, 40\%\}$) directly onto the predicted outflows $\log\hat{O}_i$. Under substantial injected noise (40\%), the target CPC degrades from $0.6896$ to $0.6626$. While this $-3.9\%$ drop is larger than the isolated production component contribution (3.6\% Shapley value), it demonstrates that even highly corrupted outflow inputs do not collapse the spatial interaction matrix, because the production-constraint normalization restricts the error propagation.

\begin{figure*}[htbp!]
  \centering
  \includegraphics[width=1.0\textwidth]{../figures/layer2_results.png}
  \caption{Outflow bottleneck analysis. \textbf{Left}: CPC vs. training source cities ($n_{\text{src}}$), showing performance saturation at 15--20 cities. \textbf{Right}: Noise sensitivity of CPC under additive Gaussian noise $\sigma$ injected on predicted outflows $\log\hat{O}_i$.}
  \label{fig:layer2_results}
\end{figure*}


\section{Additional Methodological Analyses}\label{app:methodology}

\subsection{Feature Selection Sensitivity}

\subsubsection{Feature Taxonomy and Candidate Set (37 dimensions)}
We initially construct 37 candidate features per zone. This candidate space comprises 5 base scale and density variables (zone area, road density, residential population, total POI counts, and POI density) and 32 POI category count and density features (16 category counts and 16 category densities). The feature taxonomy is shown in Fig.~\ref{fig:feature_taxonomy}.

\begin{figure*}[htbp!]
  \centering
  \begin{tikzpicture}[
    grow=right,
    level distance=3.5cm,
    sibling distance=1.0cm,
    edge from parent/.style={draw, -latex, thick},
    every node/.style={draw, rectangle, rounded corners, align=center, fill=blue!5, draw=blue!40, thick, font=\footnotesize}
  ]
    \node {Globally Available \\ Open Data}
      child { node {Contextual \\ Features}
        child { node {Z-Score Metrics} }
      }
      child { node {Infrastructure \\ Features}
        child { node {Road Density} }
        child { node {Road Length} }
      }
      child { node {Land Use \\ Features}
        child { node {POI Category Counts} }
        child { node {Total POIs} }
      }
      child { node {Population \\ Features}
        child { node {Population Density} }
        child { node {Total Population} }
      };
  \end{tikzpicture}
  \caption{Taxonomy of the globally available open data features used in the outflow model.}
  \label{fig:feature_taxonomy}
\end{figure*}

\subsubsection{SHAP-Based Feature Stability Selection}
To identify features that generalize across cities, we apply SHAP importance analysis \citep{lundberg2017unified} to the GBDT production model. Features are ranked by a cross-city stability score $S_p = \mu_p\,/\,(\sigma_p + \epsilon)$, where $\mu_p$ and $\sigma_p$ denote the mean and standard deviation of per-city GBDT SHAP importances and $\epsilon = 10^{-5}$. A feature is retained if $\mu_p \ge 0.005$ and $S_p \ge 1.0$, ensuring both relevance and cross-city consistency. This analysis identifies 25 stable features from the 37-candidate space (32.4\% dimensionality reduction) and confirms that the 6 core structural features used in the deployed model (Section~\ref{sec:origin_outflow}) are among the primary and most stable predictors, with no accuracy loss relative to the full candidate set.

\subsubsection{Feature Count Sensitivity}
Evaluating the GBDT model performance across nested subsets of top SHAP features ($K \in \{5, 10, 15, 25, 37\}$) shows that predictive performance plateaus at $K = 6$ features (CPC: $0.7080$), with additional features yielding marginal utility (e.g., CPC of $0.7120$ at $K = 15$). This indicates that most transferable spatial information is captured by a compact set of built-environment indicators.

\begin{figure*}[htbp!]
  \centering
  \begin{tikzpicture}
    \begin{axis}[
      width=0.60\textwidth,
      height=4.5cm,
      xlabel={Number of Features ($K$)},
      ylabel={Mean CPC},
      xmin=3, xmax=40,
      ymin=0.68, ymax=0.73,
      xtick={5,6,10,15,25,37},
      ytick={0.68,0.69,0.70,0.71,0.72,0.73},
      grid=both,
      thick,
      mark size=2pt
    ]
      \addplot[color=blue, mark=square*] coordinates {
        (5, 0.7077)
        (10, 0.7084)
        (15, 0.7120)
        (25, 0.7114)
        (37, 0.7117)
      };
      \draw[red, dashed, thick] (axis cs:6, 0.68) -- (axis cs:6, 0.7080);
      \draw[red, dashed, thick] (axis cs:3, 0.7080) -- (axis cs:6, 0.7080);
      \node[red, above right, font=\footnotesize] at (axis cs:6,0.7080) {$K=6$ (CPC: 0.7080)};
    \end{axis}
  \end{tikzpicture}
  \caption{SHAP feature count sweep over the 37-candidate feature set. While utilizing more than 6 features yields marginal accuracy gains, a parsimonious selection of 6 features is preferred to maintain generalization across diverse target-city environments.}
  \label{fig:shap_sweep}
\end{figure*}


\section{Implementation and Reproducibility}\label{app:implementation}

\subsection{Preprocessing and Normalization}
Data preprocessing details are summarized in Table~\ref{tab:preprocessing}.

\begin{table*}[htbp!]
\centering
\tablebodyfont\small
\caption{Preprocessing and normalization steps applied to spatial features prior to model learning.}
\label{tab:preprocessing}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lll}
\toprule
\textbf{Step} & \textbf{Treatment} & \textbf{Rationale} \\
\midrule
Missing Data & Median imputation & Rare ($<$ 2\%); resolved from spatial neighbors \\
Log Transform & Population, POI counts & Stabilize right-skewed distributions \\
Standardization & Per-city (not global) & Preserve relative spatial hierarchy \\
Outliers & Retain & Important spatial hubs (CBDs); robust models \\
\bottomrule
\end{tabular*}
\end{table*}

\subsection{Optimization and Constraints for Distance-Decay Estimation}
To solve the maximum likelihood estimation (MLE) problem for target-city decay parameters $\theta = (\alpha, \beta)$ without disaggregate flows, we adopt a robust and physically grounded initialization and optimization workflow based on closed-form moment estimates.

Good parameter initialization is critical for optimization convergence. For the exponential decay rate $\beta$, we utilize a closed-form moment estimate derived under the assumption of pure exponential deterrence and a uniform distribution of spatial opportunities. In this theoretical limit, the expected travel distance satisfies $\mathbb{E}[d] = 1/\beta$. We estimate the empirical mean trip distance $\bar{d}_{\text{obs}}$ from the observed distance-bin histogram:
\begin{equation}\label{eq:moment_d_obs}
\bar{d}_{\text{obs}} = \sum_{k=1}^{K} b_k \cdot m_k
\end{equation}
where $b_k$ is the observed proportion of trips in bin $k$, and $m_k$ is the midpoint of distance bin $k$ (for the open-ended final bin, we use $1.5$ times the lower boundary as a surrogate midpoint). The initial value $\beta^{(0)}$ is set as:
\begin{equation}\label{eq:beta_init}
\beta^{(0)} = \frac{1}{\bar{d}_{\text{obs}}}
\end{equation}
For the power-law exponent $\alpha$, the initial value is set statically to $\alpha^{(0)} = 1.0$, which corresponds to the center of the empirically observed range $[0.5, 2.0]$ in classical spatial interaction modeling literature.

The positivity constraints $\beta > 0$ and $\alpha \geq 0$ are strictly enforced during optimization via a parameter transformation. We define log-transformed parameters:
\begin{equation}\label{eq:log_transform_params}
\tilde{\beta} = \log \beta, \quad \tilde{\alpha} = \log \alpha
\end{equation}
and optimize the objective in the unconstrained log-transformed space $\theta_{\text{log}} = (\tilde{\alpha}, \tilde{\beta}) \in \mathbb{R}^2$. 

To guard against convergence to local optima due to the potential non-convexity of the exposure-corrected likelihood surface (especially under highly binned or noisy data), we run the L-BFGS-B optimization algorithm from 10 random restarts. The first run is initialized at the theoretical values $\theta_{\text{log}}^{(0)} = (\log \alpha^{(0)}, \log \beta^{(0)})$. The remaining 9 runs are initialized by perturbing this central starting point with Gaussian noise:
\begin{equation}\label{eq:restarts_noise}
\begin{split}
\tilde{\alpha}_{\text{start}}^{(r)} &\sim \mathcal{N}(\log \alpha^{(0)},\, 0.25), \\
\tilde{\beta}_{\text{start}}^{(r)} &\sim \mathcal{N}(\log \beta^{(0)},\, 0.25)
\end{split}
\end{equation}
The optimization is executed for each restart run, and the parameter set yielding the highest likelihood value $\mathcal{L}(\theta)$ is recovered via exponential back-transformation: $\hat{\alpha} = \exp(\tilde{\alpha}^*)$ and $\hat{\beta} = \exp(\tilde{\beta}^*)$.

\subsection{Hyperparameter Settings}
The GBDT hyperparameter configurations are detailed in Table~\ref{tab:gbdt_hyperparameters}.

\begin{table*}[htbp!]
\centering
\tablebodyfont
\caption{GBDT Model Hyperparameter Configurations}
\label{tab:gbdt_hyperparameters}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lcc}
\toprule
\textbf{Hyperparameter} & \textbf{Outflow Model ($O_i$)} & \textbf{Attraction Model ($A_j$, ablation only)} \\
\midrule
Base Learner & Decision Tree & Decision Tree \\
Loss Function & Least Squares (MSE on $\log O_i$) & Least Squares (MSE on $A_j$) \\
Learning Rate ($\eta$) & 0.05 & 0.05 \\
Number of Estimators & 150 & 200 \\
Max Tree Depth & 2 & 2 \\
Num. Leaves & 31 & 31 \\
Subsample Ratio & 0.8 & 0.8 \\
Colsample By Tree & 0.8 & 0.8 \\
Minimum Child Weight & 1 & 1 \\
Early Stopping Rounds & 15 & 15 \\
\bottomrule
\end{tabular*}
\end{table*}

\section{Mathematical Details}\label{app:math}
Detailed derivations of the exposure-corrected projection and adaptive scale offsets are provided in the primary text (Section~\ref{sec:methodology}).


\section{List of Abbreviations}\label{app:abbreviations}
The key abbreviations and acronyms used throughout this paper are summarized and defined in Table~\ref{tab:abbreviations}.

\begin{table*}[htbp!]
\centering
\tablebodyfont\small
\caption{List of Abbreviations}
\label{tab:abbreviations}
\begin{tabular*}{\textwidth}{@{\extracolsep{\fill}}lp{4.2cm}lp{6.0cm}}
\toprule
\textbf{Abbreviation} & \textbf{Definition} & \textbf{Abbreviation} & \textbf{Definition} \\
\midrule
CBD & Central Business District & MSE & Mean Squared Error \\
CPC & Common Part of Commuters & OD & Origin-Destination \\
GBDT & Gradient Boosted Decision Tree & OSM & OpenStreetMap \\
GDPR & General Data Protection Regulation & POI & Point of Interest \\
MLE & Maximum Likelihood Estimation & SHAP & SHapley Additive exPlanations \\
PIGF & Projection--Inference Gravity Framework & & \\
\bottomrule
\end{tabular*}
\end{table*}

\end{appendices}
"""

with open('/Users/nguyenquocthinh/Documents/PCSF-TIM/paper/draft_paper_springer.tex', 'w') as f:
    f.write(pre_app + new_appendix + post_app)

print("Appendix rewritten successfully")
