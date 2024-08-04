import typing as t
from langchain_core.vectorstores import VectorStoreRetriever
from langchain_core.documents import Document
from langchain_core.callbacks.manager import (
    CallbackManagerForRetrieverRun,
)
from langchain_core.pydantic_v1 import Field
from langchain_core.vectorstores import VectorStore


class VectorStoreRetrieverWithFilter(VectorStoreRetriever):
    """Base Retriever class for VectorStore with Filter searching."""

    vectorstore: VectorStore
    """VectorStore to use for retrieval."""
    search_type: str = "similarity"
    """Type of search to perform. Defaults to "similarity"."""
    search_kwargs: dict = Field(default_factory=dict)
    """Keyword arguments to pass to the search function."""
    allowed_search_types: t.ClassVar[t.Collection[str]] = (
        "similarity",
        "similarity_score_threshold",
        "mmr",
    )
    

    def _get_relevant_documents(
        self, query: str, *, run_manager: CallbackManagerForRetrieverRun, filter:t.Dict=None, fetch_k:int=4
    ) -> t.List[Document]:
        if self.search_type == "similarity":
            docs = self.vectorstore.similarity_search(query, filter=filter, fetch_k=fetch_k, **self.search_kwargs)
        elif self.search_type == "similarity_score_threshold":
            docs_and_similarities = (
                self.vectorstore.similarity_search_with_relevance_scores(
                    query, filter=filter, fetch_k=fetch_k, **self.search_kwargs
                )
            )
            docs = [doc for doc, _ in docs_and_similarities]
        elif self.search_type == "mmr":
            docs = self.vectorstore.max_marginal_relevance_search(
                query, filter=filter, fetch_k=fetch_k, **self.search_kwargs
            )
        else:
            raise ValueError(f"search_type of {self.search_type} not allowed.")
        return docs


def _vectorstore_to_filter_retriever(vectorstore, vectorstore_tags, **kwargs):
    tags = kwargs.pop("tags", None) or [] + vectorstore_tags
    return VectorStoreRetrieverWithFilter(vectorstore=vectorstore, tags=tags, **kwargs)