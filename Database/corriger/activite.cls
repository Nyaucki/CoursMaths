\ProvidesClass{activite}

\LoadClass[a4paper,12pt]{article}

\RequirePackage{etex}
\RequirePackage[utf8]{inputenc}
\RequirePackage[french]{babel}
\RequirePackage{fancyhdr}
\RequirePackage{pstricks,pstricks-add}
\RequirePackage{geometry}
\RequirePackage{dsfont}
\RequirePackage{pstricks}
\RequirePackage{pst-fill,pst-grad}
\RequirePackage{lmodern}
\RequirePackage[T1]{fontenc}
\RequirePackage{amsmath,amssymb,amsfonts}
\RequirePackage{graphicx}
\RequirePackage{amsthm}
\RequirePackage{xcolor}
\RequirePackage{colortbl}
\RequirePackage{tikz,tkz-tab}
\usetikzlibrary{math,calc}%Pour définir variables dans Tikz +homotetie
\RequirePackage{multicol}
\RequirePackage{array}
\RequirePackage{subfigure}
\RequirePackage{framed}
\RequirePackage{float}
\RequirePackage{eurosym}
\RequirePackage{enumerate}
\RequirePackage[explicit]{titlesec}
\RequirePackage{eso-pic}
\RequirePackage{hyperref}
\RequirePackage{fancybox}
\RequirePackage{wrapfig}
\RequirePackage{nopageno}
\RequirePackage{listings}
\RequirePackage{xargs}
\RequirePackage{pifont}
\RequirePackage{enumitem}
\RequirePackage{lipsum}
\RequirePackage{ifthen}

\newif\if@pythontex \@pythontexfalse
\DeclareOption{pythontex}{\@pythontextrue}
\DeclareOption*{}%% Ne rien faire quand une option est inconnue
\ProcessOptions

\if@pythontex
  \RequirePackage{pythontex}
\fi

\newcolumntype{Y}{>{\centering\arraybackslash}X}

\newcounter{excntr}%(a)
    \newcommand*{\cnt}{\stepcounter{excntr}{(\alph{excntr})~~}}
\newcounter{exrcntr}%counter d'exo
    \newcommand*{\exo}[2]{\bigskip \stepcounter{exrcntr}{\textbf{Exercice~\arabic{exrcntr}~:~}(#1 points) \textit{#2}}\setcounter{excntr}{0}}

\newcommand{\compeval}[2]
{\begin{tikzpicture}
    \draw[fill=gray](-1,0)--(2*#1,0)--(2*#1,0.25)--(-1,0.25)--(-1,0);
    \draw(-1,0)--(2,0)--(2,0.25)--(-1,0.25) node[midway,above] {#2}--(-1,0);
    \draw (2.6,0.125) circle (0.4);
    \draw (2.45,0.22) circle (0.1);
    \draw (2.75,0.22) circle (0.1);
    \draw (2.8,0) arc (0:-180:0.2);
    \draw (2.4,0)--(2.8,0);
    \draw (-1.6,0.125) circle (0.4);
    \draw (-1.45,0.22) circle (0.1);
    \draw (-1.75,0.22) circle (0.1);
    \draw (-1.4,-0.15) arc (0:180:0.2);
    \draw (-1.4,-0.15)--(-1.8,-0.15);
\end{tikzpicture}}

\lstset{literate={á}{{\'a}}1 {é}{{\'e}}1 {í}{{\'i}}1 {ó}{{\'o}}1 {ú}{{\'u}}1{Á}{{\'A}}1 {É}{{\'E}}1 {Í}{{\'I}}1 {Ó}{{\'O}}1 {Ú}{{\'U}}1{à}{{\`a}}1 {è}{{\`e}}1 {ì}{{\`i}}1 {ò}{{\`o}}1 {ù}{{\`u}}1{À}{{\`A}}1 {È}{{\'E}}1 {Ì}{{\`I}}1 {Ò}{{\`O}}1 {Ù}{{\`U}}1{ä}{{\"a}}1 {ë}{{\"e}}1 {ï}{{\"i}}1 {ö}{{\"o}}1 {ü}{{\"u}}1{Ä}{{\"A}}1 {Ë}{{\"E}}1 {Ï}{{\"I}}1 {Ö}{{\"O}}1 {Ü}{{\"U}}1{â}{{\^a}}1 {ê}{{\^e}}1 {î}{{\^i}}1 {ô}{{\^o}}1 {û}{{\^u}}1{Â}{{\^A}}1 {Ê}{{\^E}}1 {Î}{{\^I}}1 {Ô}{{\^O}}1 {Û}{{\^U}}1{œ}{{\oe}}1 {Œ}{{\OE}}1 {æ}{{\ae}}1 {Æ}{{\AE}}1 {ß}{{\ss}}1{ű}{{\H{u}}}1 {Ű}{{\H{U}}}1 {ő}{{\H{o}}}1 {Ő}{{\H{O}}}1{ç}{{\c c}}1 {Ç}{{\c C}}1 {ø}{{\o}}1 {å}{{\r a}}1 {Å}{{\r A}}1{€}{{\EUR}}1 {£}{{\pounds}}1}
\lstdefinestyle{stylepython}{language=Python,basicstyle=\ttfamily , commentstyle=\color{green},keywordstyle=\color{blue},stringstyle=\color{olive},    numberstyle=\tiny, numbers=left, stepnumber=1,numbersep=5pt,showstringspaces=false}



%\RequirePackage[Rejne]{fncychap}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%% PARAMETRES PAQUETS %%%%%%%%%%%%
\frenchbsetup{StandardLists=true}
\usetikzlibrary{shapes}
\usetikzlibrary{arrows}
\usetikzlibrary{patterns}
\usetikzlibrary{decorations}
\usetikzlibrary{decorations.pathmorphing}
\usetikzlibrary{decorations.pathreplacing}
\usetikzlibrary{decorations.shapes}
\usetikzlibrary{decorations.text}
\usetikzlibrary{decorations.markings}
\usetikzlibrary{decorations.fractals}
\usetikzlibrary{decorations.footprints}
\usetikzlibrary{spy}

\everymath{\displaystyle\everymath{}}
\geometry{margin=1cm}

\setitemize[1]{label=\ding{228}}
\setitemize[2]{label=\ding{223}}
\geometry{bottom=1.5cm}
\fancypagestyle{plain}{
\setlength{\footskip}{1.2cm}
\renewcommand{\footrulewidth}{1pt}
\renewcommand{\headrulewidth}{0pt}
\lhead{}
\chead{}
\rhead{}
\rfoot{\thepage}
\cfoot{}
\lfoot{}
\pagestyle{plain}
}
%%%%%%%%%%%%%% COULEURS %%%%%%%%%%%%%%%%%%%



%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%

% NUMEROS SECTION
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\renewcommand{\vec}{\overrightarrow}
\newcommand{\cc}{\mathbb{C}}
\newcommand{\rr}{\mathbb{R}}
\newcommand{\qq}{\mathbb{Q}}
\newcommand{\zz}{\mathbb{Z}}
\newcommand{\nn}{\mathbb{N}}
\newcommand{\kk}{\mathbb{K}}
\renewcommand{\aa}{\mathbb{A}}
\newcommand{\pp}{\mathbb{P}}
\newcommand{\fct}[3]{\begin{array}{rclc} #1 : & #2 & \rightarrow & #3 \end{array}}
\newcommand{\fval}[5]{\begin{array}{rclc} #1 : & #2 & \rightarrow & #3 \\ {} & #4 & \mapsto & #5 \end{array}}
\newcommand{\mk}[1]{\mathfrak{#1}}
\newcommand{\mc}[1]{\mathcal{#1}}
\newcommand{\bb}[1]{\mathbb{#1}}
\DeclareMathOperator{\id}{Id}
\newcommand{\dd}{\text{d}}
\newcommand{\g}[1]{\mathbf{#1}}
\newcommand{\vcoord}[2]{\begin{pmatrix} #1 \\ #2 \end{pmatrix}}

%%%%%%%%%%% SECTION %%%%%%%%
\renewcommand{\thesection}{\large \Roman{section}}
\renewcommand{\section}[1]{
\vspace{0.5cm}
\addtocounter{section}{1}
\setcounter{subsection}{0}
\hfill
\fbox{
\begin{minipage}{0.9\textwidth}
\begin{center}
\textsc{#1}
\end{center}
\end{minipage}
}
\hfill
\vspace{1cm}
}
	