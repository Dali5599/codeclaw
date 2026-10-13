import numpy as np
from scipy.sparse import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from codeclaw.indexer import WorkspaceSymbolIndexer

class SemanticCodeSearchProvider:
    def __init__(self, config: CodeClawConfig) -> None:
        self.config = config
        self.vectorizer = TfidfVectorizer(stop_words='english')

    def build(self) -> csr_matrix:
        """Build the TF-IDF matrix for keyword extraction."""
        keywords = self.config.default_model.split(',') if not isinstance(self.config.default_model, str) else [self.config.default_model]
        vectorizer = self.vectorizer
        tfidf_matrix = vectorizer.fit_transform(keywords)
        return tfidf_matrix
    def search(self, code: str, keywords: list[str]) -> list[tuple[int, int, str]]:
        """Search for occurrences of *keywords* in the given *code*.\n
        Returns a list of (line_number, column_offset) tuples where each keyword is found.
        \n        :param code: The source code to search through.
        :param keywords: A list of keywords to search for.
        :return: A list of occurrences of the keywords in the given *code*.
        """
        vectorizer = self.vectorizer
        tfidf_matrix = vectorizer.transform([code])
        scores = np.dot(tfidf_matrix, tfidf_matrix.T)
        return self._lookup(scores, keywords)
    def _lookup(self, scores: csr_matrix, keywords: list[str]) -> list[tuple[int, int, str]]:
        """Perform a linear search on the *scores* to find occurrences of each keyword.

        This is a simple implementation and may not be efficient for large datasets.
        \n        :param scores: The TF-IDF matrix representing the similarity between keywords and code.
        :param keywords: A list of keywords to search for.
        :return: A list of occurrences of each keyword in the given *code*.
        """
        occurrences = []
        for i, keyword in enumerate(keywords):
            line_number = int(np.argmax(scores[i]))
            column_offset = np.where(scores[i] == scores[i][line_number])[0][0]
            occurrences.append((line_number + 1, column_offset + 1, keyword))
        return occurrences
