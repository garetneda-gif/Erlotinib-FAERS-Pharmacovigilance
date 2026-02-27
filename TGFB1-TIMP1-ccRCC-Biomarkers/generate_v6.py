#!/usr/bin/env python3
"""Generate two-column paginated HTML v6 - 10 pages, optimized content distribution.

Key changes from v5 (13 pages → 10 pages):
- P1: Cover only (no intro) – prevents overflow
- P2: Full Intro + all Methods in two-column (LH=2.1)
- P3-P5: Same as v5
- P6: Fig 7 + ROC text + Fig 8 (two figures per page)
- P7: Pearson + enrichment + Fig 9 + Results 3.5 intro
- P8: Table 2 + docking text + Fig 10 + Discussion P1
- P9: Discussion P2-P7 + Conclusion + Back matter (merged)
- P10: All References 1-40 (merged)
"""

import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from generate_v2 import CSS, IMG_BASE, FIG_CAP, REFS, fig, side_by_side, header, footer

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))


def page1():
    """Cover page + Introduction."""
    return f'''
<div class="page">
    <div class="page-content" style="line-height:1.4;display:flex;flex-direction:column;">
        <div id="cover">
            <div style="display:flex;justify-content:space-between;align-items:flex-end;font-size:7pt;border-bottom:0.5pt solid #000;padding-bottom:1mm;margin-bottom:2mm;">
                <div style="flex:1;">February 2026 <span style="margin-left:2em;">DOI: 10.65079/xxx</span></div>
                <div style="font-weight:bold;">MedBA Medicine</div>
            </div>
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:6mm;">
                <div style="font-size:10pt;font-weight:bold;letter-spacing:0.06em;text-transform:uppercase;margin-top:2mm;color:#000;text-decoration:underline;text-underline-offset:2mm;">ORIGINAL ARTICLE</div>
                <img src="https://medbam.org/assets/logo.png" alt="MedBA Logo" style="height:38px;width:auto;display:block;">
            </div>
            <div id="article-title" style="font-size:18pt;font-weight:bold;margin-bottom:8mm;line-height:1.2;text-align:left;">Identification of TGFB1 and TIMP1 as the Biomarkers of Clear Cell Renal Cell Carcinoma by Bioinformatic Methods</div>
            <div id="article-authors" style="font-size:11pt;margin-bottom:10mm;font-weight:normal;text-align:left;">Lifang Zhou<sup>1</sup>, Nana Li<sup>1</sup>, Yiying Zhang<sup>1</sup>, Hongling Hu<sup>1</sup>, Hongjian Zhang<sup>1,#</sup></div>
            <div id="front-matter" style="display:flex;margin-bottom:8mm;align-items:stretch;">
                <div style="width:30%;font-size:8pt;line-height:1.3;padding:4mm 4mm 4mm 0;border-right:0.5pt solid #000;">
                    <p style="margin:0 0 3mm 0;text-indent:0;text-align:left;"><span style="vertical-align:super;font-size:0.7em;line-height:0;">1</span> Department of Cancer, Zhongshan Hospital of Xiamen University, Xiamen, China.</p>
                    <p style="margin:0 0 3mm 0;text-indent:0;text-align:left;"><span style="font-weight:bold;display:block;margin-bottom:1mm;">Correspondence</span>Hongjian Zhang, MD, Zhongshan Hospital of Xiamen University, Xiamen, 361000, China.<br>Email: zhanghongjian11021@163.com</p>
                    <p style="margin:0 0 3mm 0;text-indent:0;text-align:left;"><span style="font-weight:bold;display:block;margin-bottom:1mm;">Funding information</span>This study was supported by the Xiamen Medical and Health Guidance Project, China (Grant NO. 3502Z20254ZD1124).</p>
                </div>
                <div id="abstract-box" style="width:70%;padding:4mm;position:relative;background-color:#f8f9fa;">
                    <div style="font-size:10pt;font-weight:bold;font-variant:small-caps;letter-spacing:0.05em;margin-bottom:3mm;color:#000;">Abstract</div>
                    <div id="abstract-body" style="font-size:9pt;line-height:1.3;">
                        <p style="margin:0 0 3mm 0;text-indent:0;text-align:justify;">Clear cell renal cell carcinoma (ccRCC) is the most common histological subtype of kidney cancer and is associated with high mortality and poor prognosis. In this study, we aimed to identify potential biomarkers and therapeutic candidates for ccRCC through integrated bioinformatic analyses and molecular docking. Microarray datasets from the Gene Expression Omnibus (GEO) database were analyzed to identify differentially expressed genes (DEGs), followed by validation using The Cancer Genome Atlas (TCGA) database. A total of 608 overlapping DEGs, including 267 upregulated and 341 downregulated genes, were identified across the GSE11024, GSE16441, and GSE36895 datasets. Among these, TGFB1 and TIMP1 were identified as key genes closely associated with ccRCC progression. TCGA analyses further confirmed that TGFB1 and TIMP1 expression levels were significantly correlated with ccRCC occurrence and progression and exhibited high expression specificity. In addition, potential therapeutic compounds targeting TGFB1 and TIMP1 were screened, and molecular docking analyses demonstrated that Bosentan and Ramipril formed stable hydrogen bonds with TGFB1, while Meclizine and AM-630 showed favorable binding interactions with TIMP1. These findings suggest that TGFB1 and TIMP1 may serve as promising biomarkers and therapeutic targets for ccRCC, providing new insights into its diagnosis and targeted treatment.</p>
                        <div style="margin-top:2mm;"><span style="font-weight:bold;">Keywords:</span> Clear cell renal cell carcinoma, Metastasis, Biomarkers, Active drugs, Molecular docking</div>
                    </div>
                </div>
            </div>
        </div>
        <div class="two-column" style="flex:1;min-height:0;overflow:hidden;line-height:1.6;">
            <h1 class="section-title">1 INTRODUCTION</h1>
            <p class="no-indent">Renal malignancies are among the ten most common cancers worldwide, accounting for approximately 2% of all human tumors [1]. According to global cancer statistics in 2020, about 431,288 new cases of renal cancer were diagnosed, with approximately 179,368 related deaths [2]. Clear cell renal cell carcinoma (ccRCC) is the most prevalent subtype of renal cell carcinoma, representing nearly 75% of cases [3]. Although radical or partial nephrectomy remains the primary treatment for localized ccRCC, approximately one-third of patients eventually develop distant metastases, resulting in limited therapeutic options and poor prognosis [4]. Despite advances in targeted therapies, drug resistance has emerged as a major clinical challenge, highlighting the urgent need to identify novel biomarkers and therapeutic strategies for ccRCC.</p>
            <p>With the rapid development of next-generation sequencing technologies, high-throughput transcriptomic analyses have been widely applied in cancer research [5]. Publicly available databases, such as The Cancer Genome Atlas (TCGA) and the Gene Expression Omnibus (GEO), provide large-scale gene expression data that facilitate systematic bioinformatic investigations into cancer-related molecular mechanisms [6]. Although numerous bioinformatic studies have explored the molecular characteristics of ccRCC, most have focused on identifying diagnostic or prognostic biomarkers, while relatively few have investigated potential therapeutic agents targeting these key genes.</p>
            <p>In the present study, integrated bioinformatic analyses were performed to identify key genes associated with ccRCC progression and to explore potential therapeutic compounds. Differentially expressed genes were identified using multiple GEO datasets and subsequently validated in the TCGA database. Candidate drugs targeting the key genes were further screened, and molecular docking analyses were conducted to evaluate their binding potential. Overall, this study aims to provide new insights into the diagnosis and targeted treatment of ccRCC.</p>
        </div>
    </div>
{footer(1)}
</div>'''


def page2():
    """Methods 2.1-2.7 only (Introduction moved to P1)."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:2.4;">
        <h1 class="section-title">2 MATERIALS AND METHODS</h1>
        <h2 class="subsection-title">2.1 Microarray data collection and identification of shared DEGs</h2>
        <p class="no-indent">The microarray datasets GSE11024, GSE16441, and GSE36895 were downloaded from the GEO database (https://www.ncbi.nlm.nih.gov/geo/). The corresponding platforms were GPL6671 (Affymetrix GeneChip Human Genome U133 Plus 2.0 Array) for GSE11024, GPL6480 (Agilent-014850 Whole Human Genome Microarray 4&times;44K G4112F) for GSE16441, and GPL570 (Affymetrix Human Genome U133 Plus 2.0 Array) for GSE36895. Differentially expressed genes (DEGs) between ccRCC tissues and normal renal tissues were identified using the GEO2R online analysis tool, which is based on the R programming language. The screening criteria were set as |log&#x2082; fold change (FC)| &gt; 1 and adjusted <em>P</em>-values &lt; 0.05 [7]. The R software (version 4.2.0) and the <em>ggplot2</em> package were used to generate volcano plots for visualization of the DEGs. Subsequently, overlapping DEGs among the three datasets were identified using a Venn diagram analysis.</p>
        <h2 class="subsection-title">2.2 Enrichment analysis of shared DEGs</h2>
        <p class="no-indent">Gene Ontology (GO) is a widely used system for the functional classification of genes [8], while the Kyoto Encyclopedia of Genes and Genomes (KEGG) provides functional annotation at molecular and higher biological levels [9]. The overlapping DEGs were analyzed using the Database for Annotation, Visualization, and Integrated Discovery (DAVID, https://david.ncifcrf.gov/tools.jsp) to obtain GO and KEGG enrichment results. The inclusion criteria for enriched terms were <em>P</em> &lt; 0.05 and gene count &gt; 2. Enriched terms were ranked according to <em>P</em> values, and the top 10 terms from each category were visualized as bubble plots using R software.</p>
        <h2 class="subsection-title">2.3 The PPI network construction and hub genes selected</h2>
        <p class="no-indent">The shared DEGs were imported to the STRING database (http://string-db.org) [10] to evaluate protein&ndash;protein interactions, with the minimum required interaction score set at 0.400. The interaction data were downloaded and imported into Cytoscape software (version 3.9.1) [11] to construct a visual network. Key clusters within the PPI network were identified using the MCODE plugin with the following parameters: degree cutoff = 2, node score cutoff = 0.2, K-core = 2, and max depth = 100. Hub genes were further selected using the CytoHubba plugin [12, 13] based on the maximal clique centrality (MCC) algorithm, and the top 10 genes ranked by MCC score were defined as hub genes.</p>
        <h2 class="subsection-title">2.4 Expression and prognosis analysis of hub genes</h2>
        <p class="no-indent">The Gene Expression Profiling Interactive Analysis (GEPIA) platform, launched in 2017, is widely used to compare gene expression between tumor and normal tissue samples based on TCGA and GTEx datasets [14]. The University of Alabama at Birmingham CANcer data analysis Portal (UALCAN) provides protein-level expression analyses [15]. In the present study, GEPIA2 (http://gepia2.cancer-pku.cn/) and UALCAN (http://ualcan.path.uab.edu/) were utilized to validate the expression of hub genes in ccRCC. Additionally, the Kaplan&ndash;Meier Plotter (https://kmplot.com/analysis/) was employed to assess the prognostic significance of the hub genes [16].</p>
        <h2 class="subsection-title">2.5 Validation of key genes in the TCGA database</h2>
        <p class="no-indent">Transcriptional and clinical data of 613 ccRCC samples were obtained from the TCGA database (https://portal.gdc.cancer.gov/). Data preprocessing was performed in R software, which included removal of duplicate samples, exclusion of samples with missing clinical or expression data, and normalization by log&#x2082; transformation. The final expression matrix consisted of 532 ccRCC samples and 72 normal renal tissue samples. The <em>pheatmap</em> package in R was used to visualize the relationship between key genes and clinical parameters. Receiver operating characteristic (ROC) curves were generated using the <em>pROC</em> package to evaluate the expression specificity of the key genes in ccRCC. Pearson correlation analysis was performed to identify genes co-expressed with the key genes, and those with a Pearson correlation coefficient &gt; 0.5 were selected for enrichment analysis to explore the potential biological functions of the key genes [17].</p>
        <h2 class="subsection-title">2.6 Molecular docking of active drugs and targets</h2>
        <p class="no-indent">Active compounds associated with the key genes were screened using the Enrichr database (http://amp.pharm.mssm.edu/Enrichr), and the top two compounds were selected for molecular docking analysis. The crystal structures of the proteins encoded by the key genes and the 3D structures of the small molecule drugs were obtained from the RCSB Protein Data Bank (PDB, https://www.rcsb.org/) and PubChem database (https://pubchem.ncbi.nlm.nih.gov/), respectively. Molecular docking was performed using AutoDock Tools software (version 1.5.7), with the proteins defined as receptors and the compounds as ligands. For each docking simulation, fifty binding conformations were generated, and the conformation with the lowest binding energy was considered optimal. The optimal protein&ndash;ligand complexes were further visualized using PyMOL software (version 2.5.3) [18].</p>
        <h2 class="subsection-title">2.7 Statistical analysis</h2>
        <p class="no-indent">Statistical analyses were performed using R software. The differences in gene expression across clinical subgroups were assessed using the Student&rsquo;s <em>t</em>-test. A two-sided <em>P</em> value &lt; 0.05 was considered statistically significant.</p>
    </div>
{footer(2)}
</div>'''


def page3():
    """Table 1 + Results 3.1 + Figs 1+2 + Results 3.2 (no Fig 3)."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:2.8;">
        <h1 class="section-title">3 RESULTS</h1>
        <div class="table-wrapper" id="tbl-1">
            <div class="table-caption"><span class="tbl-label">Table 1.</span> A Summary of Microarray Datasets from Gene Expression Omnibus (GEO) database.</div>
            <table>
                <thead><tr><th>Series</th><th>Platform</th><th>GeneChip</th><th style="text-align:center;">Samples</th></tr></thead>
                <tbody>
                    <tr><td>GSE11024</td><td>GPL6671</td><td>Affymetrix GeneChip Human Genome U133 Plus 2.0 Array</td><td style="text-align:center;">22</td></tr>
                    <tr><td>GSE16441</td><td>GPL6480</td><td>Agilent-014850 Whole Human Genome Microarray 4&times;44K G4112F</td><td style="text-align:center;">34</td></tr>
                    <tr><td>GSE36895</td><td>GPL570</td><td>Affymetrix Human Genome U133 Plus 2.0 Array</td><td style="text-align:center;">46</td></tr>
                </tbody>
            </table>
        </div>
        <h2 class="subsection-title">3.1 Identification of DEGs</h2>
        <p class="no-indent">The GSE11024, GSE16441, and GSE36895 datasets were downloaded from the GEO database. This study included 10 ccRCC and 12 normal tissue samples from GSE11024, 17 ccRCC and 17 normal samples from GSE16441, and 23 ccRCC and 23 normal samples from GSE36895 (Table 1). Differentially expressed genes (DEGs) in each dataset were identified using the GEO2R online tool, with the cut-off criteria set as |log&#x2082; fold change (FC)| &gt; 1 and <em>P</em> &lt; 0.05. Volcano plots illustrating the DEGs in each dataset are shown in Figure 1. The overlap of up-regulated (Figure 2A) and down-regulated (Figure 2B) DEGs among the three datasets was visualized using Venn diagrams. In total, 608 shared DEGs were identified, including 267 up-regulated and 341 down-regulated genes (Supplementary Table 1).</p>
        {side_by_side(1, FIG_CAP[1], 2, FIG_CAP[2])}
        <h2 class="subsection-title">3.2 Gene enrichment analysis</h2>
        <p class="no-indent">As shown in Figure 3, GO enrichment analysis revealed that the shared DEGs were primarily involved in biological processes (BP) such as &ldquo;response to hypoxia,&rdquo; &ldquo;response to xenobiotic stimulus,&rdquo; &ldquo;response to drug,&rdquo; &ldquo;excretion,&rdquo; and &ldquo;angiogenesis.&rdquo; In the cellular component (CC) category, the DEGs were mainly enriched in &ldquo;extracellular exosome,&rdquo; &ldquo;apical plasma membrane,&rdquo; &ldquo;plasma membrane,&rdquo; and &ldquo;basolateral plasma membrane.&rdquo; Regarding molecular function (MF), the DEGs were predominantly associated with &ldquo;identical protein binding,&rdquo; &ldquo;extracellular matrix structural constituent,&rdquo; &ldquo;protein binding,&rdquo; and &ldquo;calcium ion binding.&rdquo; KEGG pathway analysis indicated that the shared DEGs were significantly enriched in &ldquo;carbon metabolism,&rdquo; &ldquo;HIF-1 signaling pathway,&rdquo; and &ldquo;metabolic pathways.&rdquo;</p>
    </div>
{footer(3)}
</div>'''


def page4():
    """Fig 3 + Results 3.3 + GEPIA2 validation text."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.9;">
        {fig(3, FIG_CAP[3])}
        <h2 class="subsection-title">3.3 Construction of PPI and identification of key genes</h2>
        <p class="no-indent">The protein&ndash;protein interaction (PPI) network of shared DEGs consisted of 558 nodes and 5,560 edges (Figure 4A). The top-ranked cluster was identified using the MCODE algorithm (Figure 4B). The top 10 hub genes were selected using the CytoHubba plugin, among which FN1, TIMP1, VEGFA, TGFB1, PECAM1, and CAV1 were up-regulated, while CXCL12, EGF, CTGF, and PLG were down-regulated across GSE11024, GSE16441, and GSE36895 datasets (Figure 4C). All top 10 hub genes identified by CytoHubba were included in the top MCODE cluster, suggesting their central roles in the ccRCC PPI network.</p>
        <p>Validation in GEPIA2 revealed that the mRNA expression levels of FN1, TIMP1, VEGFA, TGFB1, PECAM1, and CAV1 were significantly up-regulated in ccRCC tissues compared with normal tissues (Figure 5). Further analysis of these genes across different tumor stages using GEPIA2 and UALCAN indicated that only TGFB1 and TIMP1 expression levels were consistently correlated with ccRCC progression at both mRNA (Figure 6A) and protein levels (Figure 6B), suggesting their potential roles in promoting tumor progression. Kaplan&ndash;Meier survival analysis demonstrated that high expression of TGFB1 and TIMP1 was associated with poorer overall survival in ccRCC patients (Figure 6C).</p>
    </div>
{footer(4)}
</div>'''


def page5():
    """Fig 4 + Results 3.4 (both paragraphs)."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.6;">
        {fig(4, FIG_CAP[4])}
        <h2 class="subsection-title">3.4 Verification of TGFB1 and TIMP1 in the TCGA database</h2>
        <p class="no-indent">Given the pivotal roles of TGFB1 and TIMP1 in ccRCC, their expression was further validated using the TCGA dataset. A heatmap was generated to illustrate the correlation between these two genes and the TNM stage of ccRCC. After excluding samples with missing clinical information and cases with Mx (metastasis not evaluated) or Nx (regional lymph node not evaluated), a total of 529 samples were retained for TNM stage analysis (266 Stage I, 57 Stage II, 123 Stage III, 83 Stage IV). For individual TNM components, 532 samples were included for T stage (126 T1, 69 T2, 180 T3, 11 T4), 256 samples for N stage (240 N0, 16 N1), and 500 samples for M stage (421 M0, 79 M1).</p>
        <p>The heatmaps indicated that TGFB1 (Figure 7A) and TIMP1 (Figure 7B) were more highly expressed in advanced stages of ccRCC. Boxplot analyses further demonstrated that TGFB1 and TIMP1 expression levels were significantly elevated in stage III&ndash;IV compared to stage I&ndash;II (<em>P</em> = 0.0093) and in T3&ndash;T4 compared to T1&ndash;T2 (<em>P</em> = 0.0021) (Figure 7C, 7D). Moreover, TIMP1 expression was significantly higher in N1 compared to N0 (<em>P</em> = 0.033) and in M1 compared to M0 (<em>P</em> = 0.0003) (Figure 7D). In contrast, TGFB1 expression did not show significant differences across N or M stages (Figure 7C). These results suggest that TGFB1 and TIMP1 are associated with tumor progression in ccRCC, with TIMP1 exhibiting a broader correlation with TNM components.</p>
    </div>
{footer(5)}
</div>'''


def page6():
    """Figs 5+6 side-by-side + ROC text (no Fig 7)."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:2.8;">
        {side_by_side(5, FIG_CAP[5], 6, FIG_CAP[6])}
        <p class="no-indent">To evaluate the expression specificity of TGFB1 and TIMP1 in ccRCC, receiver operating characteristic (ROC) curves were constructed based on 532 ccRCC samples and 72 normal samples from the TCGA database. The area under the curve (AUC) was 0.883 for TGFB1 (Figure 8A) and 0.871 for TIMP1 (Figure 8B), indicating that both genes are specifically enriched in ccRCC and may serve as potential diagnostic biomarkers.</p>
    </div>
{footer(6)}
</div>'''


def page7():
    """Fig 7 + Fig 8 + Pearson + TGFB1/TIMP1 enrichment text."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.9;">
        {fig(7, FIG_CAP[7])}
        {fig(8, FIG_CAP[8])}
        <p class="no-indent">Pearson correlation analysis (|R| &gt; 0.5, <em>P</em> &lt; 0.05) was then performed to identify genes co-expressed with TGFB1 and TIMP1 in the TCGA dataset. Subsequent GO and KEGG enrichment analyses were conducted based on these correlated genes. For TGFB1, the biological processes were primarily related to epithelial-to-mesenchymal transition (Figure 9A), the molecular functions involved protein binding (Figure 9C), and the cellular components and signaling pathways were mainly associated with focal adhesion (Figure 9B, 9D).</p>
        <p>For TIMP1, the associated biological processes included collagen fibril organization, extracellular matrix organization, and skeletal system development (Figure 9E). The cellular components were enriched in extracellular matrix, extracellular space, and extracellular region (Figure 9F). Molecular functions included extracellular matrix structural constituent, extracellular matrix structural constituent conferring tensile strength, and collagen binding (Figure 9G). KEGG pathway analysis revealed that TIMP1-associated signaling pathways involved protein digestion and absorption, ECM&ndash;receptor interaction, and focal adhesion (Figure 9H). These results suggest that TGFB1 and TIMP1 may contribute to ccRCC progression through extracellular matrix remodeling and focal adhesion-related pathways.</p>
    </div>
{footer(7)}
</div>'''


def page8():
    """Fig 9 + Results 3.5 intro."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.9;">
        {fig(9, FIG_CAP[9])}
        <h2 class="subsection-title">3.5 Molecular docking of active drugs and targets</h2>
        <p class="no-indent">Finally, active compounds targeting TGFB1 and TIMP1 were identified using the Enrichr database. Bosentan and Ramipril exhibited favorable binding scores with TGFB1, whereas Meclizine and AM-630 showed good binding scores with TIMP1 (Table 2). To validate these interactions, the crystal structures of TGFB1 and TIMP1 were obtained from the PDB database, and the 2D structures of Bosentan, Ramipril, Meclizine, and AM-630 were retrieved from the PubChem database.</p>
    </div>
{footer(8)}
</div>'''


def page9():
    """Table 2 + docking results + Fig 10 + Discussion P1."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:2.3;">
        <div class="table-wrapper" id="tbl-2">
            <div class="table-caption"><span class="tbl-label">Table 2.</span> The significant drugs related to TGFB1 and TIMP1.</div>
            <table>
                <thead><tr><th>Drugs</th><th>CTD ID</th><th style="text-align:center;"><em>P</em>-value</th><th style="text-align:center;">Combined Score</th><th>Genes</th></tr></thead>
                <tbody>
                    <tr><td>Bosentan</td><td>00003071</td><td style="text-align:center;">5.50E-04</td><td style="text-align:center;">150029.821</td><td>TGFB1</td></tr>
                    <tr><td>Ramipril</td><td>00007148</td><td style="text-align:center;">5.50E-04</td><td style="text-align:center;">150029.821</td><td>TGFB1</td></tr>
                    <tr><td>Meclizine</td><td>00006252</td><td style="text-align:center;">5.50E-04</td><td style="text-align:center;">150029.821</td><td>TIMP1</td></tr>
                    <tr><td>AM-630</td><td>00003207</td><td style="text-align:center;">6.50E-04</td><td style="text-align:center;">146675.876</td><td>TIMP1</td></tr>
                </tbody>
            </table>
        </div>
        <p class="no-indent">Molecular docking was performed using AutoDock software, with TGFB1 and TIMP1 defined as receptors and the compounds as ligands. The results demonstrated that Bosentan and Ramipril formed hydrogen bonds with the amino acid residues THR-55 and VAL-79 of TGFB1, with binding energies of &minus;3.25 kcal/mol and &minus;3.2 kcal/mol, respectively (Figure 10A, 10B). Similarly, Meclizine and AM-630 formed hydrogen bonds with THR-98 and PHE-73 of TIMP1, exhibiting binding energies of &minus;8.18 kcal/mol and &minus;7.14 kcal/mol, respectively (Figure 10C, 10D). These findings suggest that these compounds may interact specifically with TGFB1 and TIMP1, providing potential therapeutic options for ccRCC.</p>
        {fig(10, FIG_CAP[10])}
        <h1 class="section-title">4 DISCUSSION</h1>
        <p class="no-indent">Clear cell renal cell carcinoma is the most common type of renal cancer and about 30% of patients had developed metastasis before clinical diagnosis. Even worse, about 30%-50% of the other patients would develop metastasis during follow-up diagnosis and treatment [19]. Patients with metastatic ccRCC show poor sensitivity to radiotherapy and chemotherapy, with poor prognosis and a 5-year survival rate of less than 10% [19]. Therefore, it is pressing to find new biomarkers and effective therapeutic targets for ccRCC. Nowadays, bioinformatics provides a platform to further explore the molecular mechanisms of tumors, making it possible to find biomarkers of tumors and aid oncotherapy at the genetic level [20].</p>
    </div>
{footer(9)}
</div>'''


def page10():
    """Discussion P2-P7 + Conclusion + Back matter."""
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.88;">
        <p class="no-indent">By bioinformatics methods, we identified a total of 608 shared DEGs in GSE11024, GSE16441, and GSE36895 datasets, including 267 up-regulated genes and 341 down-regulated genes. Judging from the results of GO and KEGG enrichment analysis, response to hypoxia, angiogenesis, and HIF-1 signaling pathway suggested that hypoxia was involved in the development of ccRCC. Importantly, the previous study had shown that hypoxia was closely related to tumor progression, and hypoxia-inducible factors 1 (HIF-1) played a central role in regulating the cellular response to hypoxia [21]. In the hypoxic tumor microenvironment, HIF-1 proteins were activated and thus increased the ability of tumor aggressiveness [22]. Moreover, &lsquo;Carbon metabolism&rsquo; and &lsquo;Metabolic pathways&rsquo; enriched in KEGG pathways suggested that metabolism was also essential for ccRCC. ccRCC is also regarded as a metabolic disease with major alterations in energy and lipid metabolism [23, 24].</p>
        <p>After the construction of the PPI network of shared DEGs, the top 10 hub genes were identified. The expressional differences of 9 hub genes between ccRCC tissues and normal tissues were consistent with the results of the GEPIA2 database. A total of 6 genes including FN1, TIMP1, VEGFA, TGFB1, PECAM1, and CAV1 were up-regulated in ccRCC, in which TGFB1 and TIMP1 were found to be correlated with the progression and prognosis of ccRCC. In the TCGA database, we further proved that TGFB1 and TIMP1 were highly expressed in the higher TNM stage of ccRCC and showed good expression specificity in ccRCC, which suggested that TGFB1 and TIMP1 may be the potential biomarkers of ccRCC.</p>
        <p>Transforming growth factor beta 1 (TGFB1) is a multifunctional cytokine that plays a complex role in tumor biology, acting as a tumor suppressor in early stages but promoting invasion and metastasis in advanced cancers [25]. Our findings demonstrate that TGFB1 is significantly upregulated in ccRCC and correlates with advanced TNM stage and poor prognosis. These observations are consistent with a recent clinicopathological study utilizing tissue microarrays and RNA in situ hybridization in a cohort of 158 ccRCC patients [26]. Mechanistically, the upregulation of TGFB1 in the tumor microenvironment activates both canonical (SMAD-dependent) and non-canonical signaling pathways. This activation leads to the downregulation of epithelial markers such as E-cadherin and upregulation of mesenchymal markers like N-cadherin and Vimentin, thereby disrupting cell-cell adhesion and endowing ccRCC cells with migratory and invasive capabilities [27]. In the context of the tumor microenvironment, TGFB1 additionally contributes to immune evasion by promoting regulatory T cell differentiation and suppressing cytotoxic T cell function, as previously demonstrated in renal cancer models [28, 29].</p>
        <p>TIMP metallopeptidase inhibitor 1 (TIMP1) is traditionally recognized as an endogenous inhibitor of matrix metalloproteinases (MMPs), but emerging evidence highlights its MMP-independent, pro-tumorigenic functions [30]. Our study found TIMP1 to be significantly upregulated in ccRCC, with high expression associated with lymph node metastasis, distant metastasis, and poor survival. This is consistent with a recent study by Dias et al, which demonstrated that plasma extracellular vesicle-derived TIMP-1 mRNA levels were significantly elevated in metastatic ccRCC patients compared to those with localized disease (<em>P</em> = 0.002) and in patients with larger tumors (&gt;7 cm) among the localized group (<em>P</em> = 0.020). Furthermore, higher TIMP-1 EV-derived mRNA levels were associated with reduced overall survival (<em>P</em> = 0.030), supporting its potential as a prognostic biomarker in ccRCC [31]. Notably, the detection of TIMP1 mRNA in plasma EVs suggests that TIMP1-related signals can be systemically transported, potentially influencing distant microenvironments. Although TIMP1 is classically involved in maintaining extracellular matrix (ECM) homeostasis by counterbalancing MMP activity [32], the paradoxical association of its high expression with poor prognosis suggests additional mechanisms. Our co-expression and enrichment analyses revealed that TIMP1-associated genes were predominantly involved in &ldquo;ECM-receptor interaction,&rdquo; and &ldquo;focal adhesion.&rdquo; This supports the notion that TIMP1 may act as a signaling molecule independent of MMP inhibition. Specifically, TIMP1 has been shown to bind to the cell surface tetraspanin CD63, initiating integrin &beta;1-mediated survival signaling cascades such as the PI3K/AKT and MAPK pathways, thereby promoting cell proliferation and resistance to apoptosis [33]. In ccRCC, this signaling axis could create a pro-metastatic niche by enhancing cancer cell survival during detachment from the primary tumor, facilitating the colonization of distant organs.</p>
        <p>Even though the key role of TGFB1 and TIMP1 in ccRCC, very few drugs were designed to target them. In the Enrichr database, we found that Bosentan and Ramipril were correlated with TGFB1, and Meclizine and AM-630 were correlated with TIMP1. The results of molecular docking further proved the good binding capacity of these active drugs to TGFB1 and TIMP1, suggesting that these active drugs may exert anti-tumor efficacy in ccRCC. Bosentan is an antagonist of the endothelin-1 (ET-1) receptor and is used primarily for the treatment of pulmonary arterial hypertension (PAH). A previous study proved that Bosentan combined with amlodipine could abolish the expression of TGFB1 in the kidney [34]. Similarly, this down-regulated of TGFB1 was also observed when combining Bosentan with valsartan [35]. Mechanistically, ET-1 could increase the protein and gene expression of TGFB1 and Bosentan could inhibit this effect by blocking the ET-1 receptor [36]. Ramipril is an inhibitor of angiotensin-converting enzyme (ACE) [37]. The early study proved that Ramipril exerted antiproteinuric and antifibrotic nephroprotective effects by down-regulating TGF-beta1 [38]. Meclizine is an antihistamine that reversibly inhibits the interaction of histamine with H1 receptors [39] and Iodopravadoline (AM630) is an antagonist of cannabinoid receptors [40]. However, there were few studies about their interaction with TIMP1. In all, the active drugs screened out by our study may exert an anti-tumor effect by targeting TGFB1 or TIMP1.</p>
        <p>Nevertheless, several limitations of this study should be acknowledged. First, although we utilized multiple GEO datasets and validated our findings in the TCGA cohort, heterogeneity across datasets (such as different microarray platforms and sample processing methods) may introduce potential bias into the identification of DEGs. Second, our study is primarily bioinformatic and correlative. While we identified TGFB1 and TIMP1 as key genes and performed molecular docking, the lack of in vitro and in vivo experimental validation limits our ability to draw definitive conclusions about the causal roles of these genes or the therapeutic efficacy of the screened drugs in ccRCC. Third, the molecular docking analysis provides preliminary evidence of binding affinity, but these interactions need to be confirmed by experimental techniques such as surface plasmon resonance (SPR) or cellular thermal shift assays (CETSA) to validate target engagement.</p>
        <h1 class="section-title">5 CONCLUSION</h1>
        <p class="no-indent">In summary, our findings suggest that TGFB1 and TIMP1 may be involved in the progression of ccRCC and may serve as potential biomarkers for diagnosis and therapeutic targeting. Furthermore, the candidate drugs identified in this study may provide potential directions for future therapeutic development. Nevertheless, since this study was primarily based on bioinformatics analyses of sequencing data, further experimental validation, including in vitro and in vivo studies, is necessary to confirm the biological functions of TGFB1 and TIMP1 and to evaluate the therapeutic potential of the identified drugs.</p>
        <h1 class="section-title">ETHICAL STATEMENTS</h1>
        <p class="no-indent">This study did not involve any experiments on humans or animals. All data were obtained from publicly available databases, and therefore ethical approval and informed consent were not required.</p>
        <h1 class="section-title">ACKNOWLEDGEMENTS</h1>
        <p class="no-indent">The authors have no acknowledgements to declare.</p>
        <h1 class="section-title">CONFLICTS OF INTEREST</h1>
        <p class="no-indent">The authors declare that there is no conflict of interest regarding the publication of this article.</p>
    </div>
{footer(10)}
</div>'''


def page11():
    """References 1-40 (all)."""
    refs_html = "\n            ".join(f'<div>{r}</div>' for r in REFS)
    return f'''
<div class="page">
{header()}
    <div class="page-content two-column" style="line-height:1.86;">
        <h1 class="section-title">REFERENCES</h1>
        <div class="references">
            {refs_html}
        </div>
    </div>
{footer(11)}
</div>'''


def build_html():
    pages = [page1(), page2(), page3(), page4(), page5(),
             page6(), page7(), page8(), page9(), page10(), page11()]
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Identification of TGFB1 and TIMP1 as the Biomarkers of Clear Cell Renal Cell Carcinoma by Bioinformatic Methods</title>
    <style>{CSS}    </style>
</head>
<body>
{"".join(pages)}
</body>
</html>'''


if __name__ == "__main__":
    html = build_html()
    out1 = os.path.join(OUTPUT_DIR, "双栏分页-TGFB1-TIMP1-ccRCC-Biomarkers.html")
    out2 = os.path.join(OUTPUT_DIR, "two-column.html")
    for path in [out1, out2]:
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
    print(f"Generated {len(html):,} bytes, 11 pages")
    print(f"  -> {out1}")
    print(f"  -> {out2}")
