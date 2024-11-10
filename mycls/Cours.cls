\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/Cours}

\LoadClass[a4paper,12pt]{ArticleCommande}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTINGS %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\author{}
\date{ }

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


\renewcommand{\arraystretch}{2.5}%Place dans un tableau


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

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