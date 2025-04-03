\ProvidesClass{/home/nyaucki/Documents/Prof/CoursMaths/mycls/ArticleCommande}

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
\RequirePackage{cancel}
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
\RequirePackage{refcount}
\RequirePackage{fourier}
\RequirePackage{enumitem}
\RequirePackage{pgffor} %Pour bouclke loop

\usetikzlibrary{positioning}
\usetikzlibrary{calc}%Pour extend line
\usetikzlibrary{math}%Pour définir variables dans Tikz
\usetikzlibrary{arrows.meta} %pour faire des flèches
\usetikzlibrary{babel} % permet d'éviter d'utiliser \shorthandoff{:!}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% SETTING %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\hyphenpenalty=10000 %Pas couper les mots


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% COMMANDES TIKZ %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\tikzset{ %Pour marquer les perpendiculaires
    right angle quadrant/.code={
        \pgfmathsetmacro\quadranta{{1,1,-1,-1}[#1-1]}     % Arrays for selecting quadrant
        \pgfmathsetmacro\quadrantb{{1,-1,-1,1}[#1-1]}},
    right angle quadrant=1, % Make sure it is set, even if not called explicitly
    right angle length/.code={\def\rightanglelength{#1}},   % Length of symbol
    right angle length=2ex, % Make sure it is set...
    right angle symbol/.style n args={3}{
        insert path={
            let \p0 = ($(#1)!(#3)!(#2)$) in     % Intersection
                let \p1 = ($(\p0)!\quadranta*\rightanglelength!(#3)$), % Point on base line
                \p2 = ($(\p0)!\quadrantb*\rightanglelength!(#2)$) in % Point on perpendicular line
                let \p3 = ($(\p1)+(\p2)-(\p0)$) in  % Corner point of symbol
            (\p1) -- (\p3) -- (\p2)
        }
    }
}

\tikzset{
    homothety at/.style args={#1 scaled by #2}{shift={($(#1)!#2!(0,0)$)},scale=#2},}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% AUTRES COMMANDES %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

\newcommand{\makeAlph}[1]{\@Alph{#1}}%Transforme nombre en lettre

\newcommand{\fillin}[1][2cm]{\makebox[#1]{\dotfill}}

\newcommand{\separe}{\hrule \vspace{-0.5em}}

\newcommand*{\zz}{\mathds{Z}}

\newcommand*{\nn}{\mathds{N}}

\newcommand*{\qq}{\mathds{Q}}

\newcommand*{\rr}{\mathds{R}}

\newcolumntype{Y}{>{\centering\arraybackslash}X}