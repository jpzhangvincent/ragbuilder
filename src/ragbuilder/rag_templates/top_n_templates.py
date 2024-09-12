
top_n_templates = {
    'graph_rag': {
        'name': 'Graph RAG - Graph Retriever',
        'description': 'Graph RAG (Graph Retriever only). Make sure NEO4J_LOAD=true in .env file if you are loading/reloading the data in the Graph DB',
        'module': 'graph_rag'
    },
    'graph_rag_hybrid': {
        'name': 'Graph RAG - Hybrid Retriever(Graph + Vector)',
        'description': 'Graph RAG (Graph & Vector Retriever).  Make sure NEO4J_LOAD=true in .env file if you are loading/reloading the data in the Graph DB',
        'module': 'graph_rag_hybrid'
    },
    'query_rewrite': {
        'name': 'Query Rewrite RAG',
        'description': 'In this template, we rewrite the query first to improve retrieval',
        'module': 'query_rewrite'
    },
    'rrf': {
        'name': 'Query Expansion with RRF',
        'description': 'Query Expansion with Reciprocal Rank Fusion to merge results from all queries',
        'module': 'rrf'
    },
    'step_back_prompt': {
        'name': 'Step Back Prompting',
        'description': 'Step Back Prompting',
        'module': 'step_back_prompt'
    },
    'semantic_chunker': {
        'name': 'Semantic Chunker',
        'description': 'Semantic chunker',
        'module': 'semantic_chunker'
    },
    'hyde': {
        'name': 'HyDE',
        'description': 'HyDE, or Hypothetical Document Embeddings, is a retrieval method that uses "fake" (hypothetical) documents to improve the answers generated by large language models (LLMs)',
        'module': 'hyde'
    },
    'hybrid_rag': {
        'name': 'Hybrid RAG',
        'description': 'Hybrid RAG',
        'module': 'hybrid_rag'
    }
}

def get_templates():
    return [{'id': key, 'name': value['name'], 'description': value['description']} for key, value in top_n_templates.items()]

# top_n_templates= {
# 	'hybrid_rag_langchain_v1': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Contextual Compression with vectorSimilarity and vectorMMR retrievers and LongContextReorder',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs':5},
#           {'retriever_type': 'vectorMMR', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v2': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Contextual Compression with bm25Retriever and LongContextReorder',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'bm25Retriever', 'search_type': 'similarity', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v3': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retrieve(vectorSimilarity & bm25Retriever) and LongContextReorder',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#           {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v4': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retrieve(vectorSimilarity & bm25Retriever) and Contextual compression-LongContextReorder - gpt4.0',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#           {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v5': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retrieve(vectorSimilarity & bm25Retriever) and Contextual compression-CrossEncoderReranker - gpt4.0',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#           {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['CrossEncoderReranker'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v6': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retrieve(vectorSimilarity & bm25Retriever) and Contextual compression-LongContextReorder & LLMChainFilter - gpt4.0',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#           {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LLMChainFilter', 'LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v7': {
#       'framework': 'langchain',
#       'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retrieve(vectorSimilarity & bm25Retriever) and Contextual compression-LongContextReorder & LLMChainFilter - gpt4.0',
#       'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#       'chunking_kwargs': {'chunk_strategy': 'RecursiveCharacterTextSplitter', 'chunk_size': 1000, 'chunk_overlap': 200},
#       'vectorDB_kwargs': {'vectorDB': 'chromaDB'},
#       'embedding_kwargs': {'embedding_model': 'OpenAI:text-embedding-3-large'},
#       'retriever_kwargs': {
#         'retrievers': [
#           {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#           {'retriever_type': 'vectorMMR', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['EmbeddingsRedundantFilter'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#       }
#     },
#     'hybrid_rag_langchain_v8': {
#     'framework': 'langchain',
#     'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using MultiQueryRetriever and Contextual compression-LongContextReorder & LLMChainFilter - gpt4.0',
#     'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#     'chunking_kwargs': {
#         'chunk_strategy': 'RecursiveCharacterTextSplitter',
#         'chunk_size': 1000,
#         'chunk_overlap': 200
#     },
#     'vectorDB_kwargs': {
#         'vectorDB': 'chromaDB'
#     },
#     'embedding_kwargs': {
#         'embedding_model': 'OpenAI:text-embedding-3-large'
#     },
#     'retriever_kwargs': {
#         'retrievers': [
#             {'retriever_type': 'multiQuery', 'search_type': 'similarity', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#     }},
#     'hybrid_rag_langchain_v9': {
#     'framework': 'langchain',
#     'description': 'Hybrid RAG using Langchain with RecursiveCharacterTextSplitter using Merge Retreiver(vectorSimilarity,) and Contextual compression-LongContextReorder-gpt4.0 & text-embedding-ada-002 embedding',
#     'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#     'chunking_kwargs': {
#         'chunk_strategy': 'RecursiveCharacterTextSplitter',
#         'chunk_size': 1000,
#         'chunk_overlap': 200
#     },
#     'vectorDB_kwargs': {
#         'vectorDB': 'chromaDB'
#     },
#     'embedding_kwargs': {
#         'embedding_model': 'OpenAI:text-embedding-3-large'
#     },
#     'retriever_kwargs': {
#         'retrievers': [
#             {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#             {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#     }},
#     'hybrid_rag_langchain_v10': {
#     'framework': 'langchain',
#     'description': 'Hybrid RAG using Langchain with CharacterTextSplitter using Merge Retreiver(vectorSimilarity,) and Contextual compression-LongContextReorder-gpt4.0 & text-embedding-ada-002 embedding',
#     'retrieval_model': 'OpenAI:gpt-3.5-turbo',
#     'chunking_kwargs': {
#         'chunk_strategy': 'CharacterTextSplitter',
#         'chunk_size': 1000,
#         'chunk_overlap': 200
#     },
#     'vectorDB_kwargs': {
#         'vectorDB': 'chromaDB'
#     },
#     'embedding_kwargs': {
#         'embedding_model': 'OpenAI:text-embedding-3-large'
#     },
#     'retriever_kwargs': {
#         'retrievers': [
#             {'retriever_type': 'vectorSimilarity', 'search_type': 'similarity', 'search_kwargs': 5},
#             {'retriever_type': 'bm25Retriever', 'search_type': 'mmr', 'search_kwargs': 5}
#         ],
#         'document_compressor_pipeline': ['LongContextReorder'],
#         'EmbeddingsClusteringFilter_kwargs': {'embeddings': 'OpenAI:text-embedding-3-large', 'num_clusters': 4, 'num_closest': 1, 'sorted': True},
#         'contextual_compression_retriever': True
#     }
# }



# }