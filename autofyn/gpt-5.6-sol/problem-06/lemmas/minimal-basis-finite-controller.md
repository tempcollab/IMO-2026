# Minimal-basis finite-controller criterion

Let \(\mathcal F\) be an upward-closed family of finite subsets of a ground set. Suppose there is a finite set \(P\) containing every inclusion-minimal member of \(\mathcal F\). Then, for every finite set \(H\),
\[
H\in\mathcal F\quad\Longleftrightarrow\quad H\cap P\in\mathcal F.
\]

If \(H\in\mathcal F\), repeatedly delete elements of the finite set \(H\) whenever membership in \(\mathcal F\) is preserved. This terminates at an inclusion-minimal member \(M\in\mathcal F\) with \(M\subseteq H\). By hypothesis \(M\subseteq P\), so \(M\subseteq H\cap P\), and upward closure gives \(H\cap P\in\mathcal F\). Conversely, if \(H\cap P\in\mathcal F\), then upward closure and \(H\cap P\subseteq H\) give \(H\in\mathcal F\).