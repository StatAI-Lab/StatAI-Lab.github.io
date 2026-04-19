// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-research",
          title: "Research",
          description: "Success is not final, failure is not fatal. It is the courage to continue that counts. By Winston Churchill.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/research/";
          },
        },{id: "nav-publications",
          title: "Publications",
          description: "The best thing about being a statistician is that you get to play in everyone&#39;s backyard. By John Tukey.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-software",
          title: "Software",
          description: "Open-source software, tools, and resources developed by members in Chong Wu Lab.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/software/";
          },
        },{id: "nav-team",
          title: "Team",
          description: "Meet the dedicated researchers and students driving our work forward. We are always looking for talented individuals to join us!",
          section: "Navigation",
          handler: () => {
            window.location.href = "/Team/";
          },
        },{id: "nav-grants",
          title: "Grants",
          description: "Overview of current and previous research funding supporting our work.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/grants/";
          },
        },{id: "nav-talks",
          title: "Talks",
          description: "Selected presentations and invited talks on statistical genetics, causal inference, AI for science, and related topics.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/talks/";
          },
        },{id: "news-our-r01-grant-uncovering-causal-protein-markers-to-improve-prostate-cancer-etiology-understanding-and-risk-prediction-in-africans-and-europeans-mpi-lang-wu-and-chong-wu-has-been-awarded-by-the-nci",
          title: 'Our R01 grant, “Uncovering causal protein markers to improve prostate cancer etiology understanding...',
          description: "",
          section: "News",},{id: "news-our-u01-grant-uncovering-causal-protein-markers-to-characterize-pancreatic-cancer-etiology-and-improve-risk-prediction-mpi-lang-wu-and-chong-wu-has-been-awarded-by-the-nci",
          title: 'Our U01 grant, “Uncovering Causal Protein Markers to Characterize Pancreatic Cancer Etiology and...',
          description: "",
          section: "News",},{id: "news-our-trans-pwas-work-has-been-selected-by-ashg-for-a-platform-talk-congratulations-zichen",
          title: 'Our trans-PWAS work has been selected by ASHG for a platform talk. Congratulations,...',
          description: "",
          section: "News",},{id: "news-our-pilot-grant-titled-novel-large-language-models-for-discovering-effective-drug-targets-in-prostate-cancer-has-been-awarded-by-u-foundation-thank-you-for-supporting-our-work-in-using-llms-to-accelerate-drug-discovery",
          title: 'Our pilot grant titled “Novel Large Language Models for Discovering Effective Drug Targets...',
          description: "",
          section: "News",},{id: "news-our-dna-foundation-benchmarking-paper-benchmarking-dna-foundation-models-for-genomic-and-genetic-tasks-co-corresponding-author-peng-wei-has-been-accepted-in-nature-communications-congratulations-on-your-hard-work-haonan",
          title: 'Our DNA foundation benchmarking paper, “Benchmarking DNA Foundation Models for Genomic and Genetic...',
          description: "",
          section: "News",},{id: "news-our-mendelian-randomization-method-care-winner-s-curse-free-robust-mendelian-randomization-with-summary-data-co-corresponding-author-jingshen-wang-has-been-accepted-in-journal-of-the-american-statistical-association-big-congratulations-zhongming-uc-berekely-and-wanheng-see-the-software-at-https-chongwulab-github-io-mrcare",
          title: 'Our Mendelian randomization method, CARE, “Winner’s Curse Free Robust Mendelian Randomization with Summary...',
          description: "",
          section: "News",},{id: "news-thinking-machines-lab-provides-a-small-grant-for-comptuational-resources-in-tinker-for-supporting-our-fine-tuning-efforts-thank-you-thinking-machines-lab",
          title: 'Thinking Machines Lab provides a small grant for comptuational resources in Tinker for...',
          description: "",
          section: "News",},{id: "news-our-meta-router-meta-router-bridging-gold-standard-and-preference-based-evaluations-in-large-language-model-routing-co-corresponding-author-yichi-zhang-has-been-accepted-in-iclr-2026",
          title: 'Our Meta-Router, “Meta-Router: Bridging Gold-standard and Preference-based Evaluations in Large Language Model Routing”...',
          description: "",
          section: "News",},{id: "news-our-bayesian-method-zi-hgt-for-spatial-transcriptomics-a-zero-inflated-hierarchical-generalized-transformation-model-to-address-non-normality-in-spatially-informed-cell-type-deconvolution-co-corresponding-author-jonathan-bradley-has-been-accepted-in-biometrics-big-congrats-to-hunter",
          title: 'Our Bayesian method ZI-HGT for spatial transcriptomics, “A Zero-Inflated Hierarchical Generalized Transformation Model...',
          description: "",
          section: "News",},{id: "news-our-data-resource-paper-an-atlas-of-genetic-effects-on-the-monocyte-methylome-across-european-and-african-populations-co-corresponding-author-hui-shen-and-hong-wen-deng-has-been-accepted-in-genome-medicine-congrats-to-wanheng-and-chuan-tulane-university",
          title: 'Our data resource paper, “An atlas of genetic effects on the monocyte methylome...',
          description: "",
          section: "News",},{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%63%77%75%31%38@%6D%64%61%6E%64%65%72%73%6F%6E.%6F%72%67", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/ChongWu-Biostat", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0002-8400-1785", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=sWUsT2UAAAAJ", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
