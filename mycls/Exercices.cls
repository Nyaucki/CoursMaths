\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Exercices}

\LoadClass[a4paper,12pt]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/ArticleCommande}

\RequirePackage{setspace}



%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTINGS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Changement du bloc titre
\makeatletter
\def\@maketitle{%
  \vskip -1em%
  \begin{center}%
    {\LARGE \@title ~-~Exercices \par}%
  \end{center}%
  \vskip 0.5em}
\makeatothe

\AtBeginDocument{\renewcommand\labelitemi{$\bullet$}}%Itemize avec des bullet !

\setlength{\mathindent}{0cm}


\advance\year by -1
\ifnum \the\month > 7 \advance\year by 1 \fi %pour la bonne année en bas à droite 

\newcommand\nextyear
{\advance\year by 1 \the\year\advance\year by -1}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\fancyfoot[LO]{M. Loizon}
\fancyfoot[RO]{\the\year /\nextyear}
\fancypagestyle{plain}{
  \fancyfoot[C]{\thepage}% you can add edits that won't affect "fancy" but only "plain"
}


\graphicspath{ {./Images/} }

\setlength{\columnseprule}{0.5pt}%Pour avoir la ligne séparant les multicols (0pt pour la faire disparaitre)

\setlength{\belowdisplayshortskip}{0pt} %Pour ne pas sauter autant de place sous chaque equation
\setlength{\belowdisplayskip}{0pt} 
\setlength{\abovedisplayshortskip}{0.5em} 
\setlength{\abovedisplayskip}{0.5em} 

\setstretch{0.3}

\renewcommand{\arraystretch}{1.5}%Place dans un tableau
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\filling}[1][2cm]{\makebox[#1]{\dotfill}}

\newcounter{exrcntr}
    \newcommand*{\exo}[1]{\refstepcounter{exrcntr}\vspace{0.5em}\textbf{Exercice~\arabic{exrcntr}~:~}\label{#1}}
