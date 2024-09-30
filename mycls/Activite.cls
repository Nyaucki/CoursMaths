\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Activite}

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

\graphicspath{ {./Images/} }

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt} %Pas de header ni foot

\hyphenpenalty 10000 % Pas de mots coupés
\exhyphenpenalty 10000 % Pas de mots coupés

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand*{\zz}{\mathds{Z}}

\newcommand*{\nn}{\mathds{N}}

\newcommand*{\qq}{\mathds{Q}}

\newcommand*{\rr}{\mathds{R}}

\newcolumntype{Y}{>{\centering\arraybackslash}X}

\newcounter{propcntr}%PROPRIETE
    \newtcolorbox{propriete}[1]{colback=white,colframe=gray,fonttitle=\bfseries,title=\stepcounter{propcntr} Propriété~\arabic{propcntr}~: \MakeUppercase#1}%Boite propriétés

\newcounter{defcntr}%Définition
    \newtcolorbox{definition}[1]{colback=white,colframe=lightgray,fonttitle=\bfseries,title=\stepcounter{propcntr} Définition~\arabic{propcntr}~: \MakeUppercase#1}%Boite definition

\newcounter{exmplcntr}%Exemple
    \newcommand*{\exmpl}[1]{\stepcounter{exmplcntr}{\textbf{Exemple~\arabic{exmplcntr}~:~} #1}
    \medskip}%sans liste

\newcommand{\rmq}[1]{\cours{\textbf{Remarque~:~}#1}}%Remarque

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

