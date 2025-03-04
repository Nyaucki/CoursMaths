\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/interro}

\LoadClass[a4paper,12pt]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/ArticleCommande}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTINGS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\AtBeginDocument{\renewcommand\labelitemi{$\bullet$}}%Itemize avec des bullet !

\setlength{\mathindent}{0cm}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% FOOTING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\advance\year by -1
\ifnum \the\month > 7 \advance\year by 1 \fi %pour la bonne année en bas à droite 

\newcommand\nextyear
{\advance\year by 1 \the\year\advance\year by -1}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[LO]{\the\year /\nextyear}
\fancyfoot[RO]{Attention, le sujet est recto-verso}
\fancyfoot[RO]{M. Loizon}
\fancypagestyle{plain}{
  \fancyfoot[C]{\thepage}% you can add edits that won't affect "fancy" but only "plain"
}

\setlength{\headheight}{15pt}

\graphicspath{ {./Images/} }

\setlength{\columnseprule}{0.5pt}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\filling}[1][2cm]{\makebox[#1]{\dotfill}}


\newcommand{\compeval}
{\begin{tikzpicture}
    \draw(-2,0)--(2,0)--(2,0.25)--(-2,0.25) --(-2,0);
    \draw (0,0)--(0,0.25);
    \draw (1,0)--(1,0.25);
    \draw (0,0)--(0,0.25);
    \draw (-1,0)--(-1,0.25);
    \draw (2.6,0.125) circle (0.4);
    \draw (2.45,0.22) circle (0.1);
    \draw (2.75,0.22) circle (0.1);
    \draw (2.8,0) arc (0:-180:0.2);
    \draw (2.4,0)--(2.8,0);
    \draw (-2.6,0.125) circle (0.4);
    \draw (-2.45,0.22) circle (0.1);
    \draw (-2.75,0.22) circle (0.1);
    \draw (-2.4,-0.15) arc (0:180:0.2);
    \draw (-2.4,-0.15)--(-2.8,-0.15);
\end{tikzpicture}}

\ExplSyntaxOn
\newcommand\testpoint[1]
    { \tl_if_empty:nTF {#1} {(Bonus)} {(\hspace{0.7cm}/ #1 ~ points)} }
\ExplSyntaxOff %Des points si remplis, bonus sinon

\newcounter{excntr}%(a)
    \newcommand*{\cnt}{\stepcounter{excntr}{(\alph{excntr})~~}}
\newcounter{excntrb}%(1)
    \newcommand*{\cntb}{\stepcounter{excntrb}{(\arabic{excntrb})~~}\setcounter{excntr}{0}}
\newcounter{exrcntr}%counter d'exo
    \newcommand*{\exo}[2]{\bigskip \stepcounter{exrcntr}{\textbf{Exercice~\arabic{exrcntr}~:~}\testpoint{#1} \textit{#2}~:~}\setcounter{excntr}{0}\setcounter{excntrb}{0}}



