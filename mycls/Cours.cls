\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Cours}

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

\author{}

\AtBeginDocument{\renewcommand\labelitemi{$\bullet$}}%Itemize avec des bullet !

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

\newif\ifshowcours%Pour cacher le cours
    \showcoursfalse
    \newcommand{\cours}[1]{\ifshowcours #1 \fi}
\showcourstrue%Montre le cours

\newcounter{exmplcntr}%Exemple
    \newcommand*{\exmpl}[1]{\stepcounter{exmplcntr}{\cours{\textbf{Exemple~\arabic{exmplcntr}~:~} #1}
    \medskip}}%sans liste

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