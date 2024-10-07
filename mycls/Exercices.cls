\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Exercices}

\LoadClass[a4paper,12pt]{article}

\RequirePackage[utf8]{inputenc}
\RequirePackage{babel}[french]
\RequirePackage[T1]{fontenc}
\RequirePackage{dsfont}
\RequirePackage{amsmath}
\RequirePackage[top=1cm,bottom=2cm,left=1.5cm, right=1.5cm]{geometry}
\RequirePackage{tcolorbox}
\RequirePackage{parskip}
\RequirePackage{graphicx}
\RequirePackage{float}
\RequirePackage{tikz,tkz-tab}
\RequirePackage{appendix}
\RequirePackage{tabularx}
\RequirePackage{amsmath}
\RequirePackage{rotating}
\RequirePackage{esvect}
\RequirePackage{cancel}
\usetikzlibrary{positioning}
\RequirePackage{pgfpages}
\RequirePackage{multicol}
\RequirePackage{tkz-euclide}
\RequirePackage{esvect}
\RequirePackage{enumerate}
\RequirePackage{fancyhdr}
\RequirePackage{lipsum}
\RequirePackage{amssymb}
\RequirePackage{diagbox}
\RequirePackage{mathtools}
\RequirePackage[nomessages]{fp}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTINGS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\separe}{\hrule \vspace{-0.5em}}

\newcommand*{\zz}{\mathds{Z}}

\newcommand*{\nn}{\mathds{N}}

\newcommand*{\qq}{\mathds{Q}}

\newcommand*{\rr}{\mathds{R}}

\newcolumntype{Y}{>{\centering\arraybackslash}X}

\newcommand{\markerbox}{\raisebox{-1pt}{\tikz{\node[minimum height=0.8em,minimum width=2em,draw](){};}}}%Pour noter résultat

\newcommand*{\exref}[1]{\textbf{Exercice~\ref{#1}~\markerbox} }

\newcounter{propcntr}%PROPRIETE
    \newtcolorbox{propriete}[1]{colback=white,colframe=gray,fonttitle=\bfseries,title= Propriété~: \MakeUppercase#1}%Boite propriétés

\newtcolorbox{plandetravail}[1]{colback=white,colframe=lightgray,fonttitle=\bfseries,title= #1}

\newtcolorbox{plandetravailDS}{colback=white,colframe=black,fonttitle=\bfseries,title=Contenu du DS}

\newcommand{\bidouille}[1]{Il~est~recommandé~d'en~faire~au~moins~{#1}.}

\ExplSyntaxOn
\newcommand\testrecommandation[1]
  { \tl_if_empty:nTF {#1} {} { \bidouille{#1} } }
\ExplSyntaxOff %Une solution si remplie, rien sinon

\newcommand*{\pdt}[3][]{
    \begin{plandetravail}{#2}
        \testrecommandation{#1}
        #3
    \end{plandetravail}
    }


    \newtcolorbox{definition}[1]{colback=white,colframe=lightgray,fonttitle=\bfseries,title= Définition~: \MakeUppercase#1}%Boite definition

\newcommand*{\prop}[2]{
        \begin{propriete}{#1}
            #2
        \end{propriete}
        }
   
\newcommand*{\dfnt}[2]{
    \begin{definition}{#1}
        #2
    \end{definition}
    }

\newcounter{excntr}%(a)
    \newcommand*{\cnt}{\stepcounter{excntr}{(\alph{excntr})~~}}
\newcounter{excntrb}%(1)
    \newcommand*{\cntb}{\stepcounter{excntrb}{(\arabic{excntrb})~~}\setcounter{excntr}{0}}
\newcounter{exrcntr}%counter d'exo
    \newcommand*{\exo}[2]{\bigskip \refstepcounter{exrcntr}{\vspace{0.5em}\textbf{Exercice~\arabic{exrcntr}~:~} \textit{(#1)}}\setcounter{excntr}{0}\setcounter{excntrb}{0}\label{#2}}%Rajouter un if pas correction

\hyphenpenalty=10000 %Pas couper les mots