\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Activite}

\LoadClass[a4paper,12pt]{/home/nyaucki/Documents/Prof/CoursMaths/mycls/ArticleCommande}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTINGS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\AtBeginDocument{\renewcommand\labelitemi{$\bullet$}}%Itemize avec des bullet !

\graphicspath{ {./Images/} }

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt} %Pas de header ni foot

\hyphenpenalty 10000 % Pas de mots coupés
\exhyphenpenalty 10000 % Pas de mots coupés

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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

