from langchain_mistralai.chat_models import ChatMistralAI
from langchain_huggingface import HuggingFaceEndpoint
from langchain_openai import ChatOpenAI
from ragbuilder.langchain_module.common import setup_logging,codeGen
import logging
setup_logging()
import os
logger = logging.getLogger("ragbuilder")
def getLLM(**kwargs):
    logger.info("LLM Invoked")
    retrieval_model=kwargs['retrieval_model']
    model_owner= retrieval_model.split(":")[0]
    model= retrieval_model.split(":")[1]
    if model_owner == "Groq":
        logger.info(f"LLM Code Gen Invoked:Groq")
        import_string = f"""from langchain_groq import ChatGroq""" 
        code_string = f"""llm= ChatGroq(temperature=0,model_name='{model}')"""
    elif model_owner == "Azure":
        logger.info(f"LLM Code Gen Invoked:Azure")
        import_string = f"""from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI""" 
        code_string = f"""llm= AzureChatOpenAI(model='{model}')"""
    elif model_owner == "Google":
        logger.info(f"LLM Code Gen Invoked:Google")
        import_string = f"""from langchain_google_genai import ChatGoogleGenerativeAI""" 
        code_string = f"""llm = ChatGoogleGenerativeAI(model='{model}')"""
    elif model_owner == "GoogleVertexAI":
        logger.info(f"LLM Code Gen Invoked:GoogleVertexAI")
        import_string = f"""from langchain_google_vertexai import ChatVertexAI""" 
        code_string = f"""llm = ChatVertexAI(model_name='{model}')"""
    elif model_owner == "OpenAI":
        logger.info(f"LLM Code Gen Invoked: {retrieval_model}")
        import_string = f"""from langchain_openai import ChatOpenAI""" 
        code_string = f"""llm=ChatOpenAI(model='{model}')"""
    elif model_owner == "Mistral":
        logger.info(f"LLM Code Gen Invoked: {retrieval_model}")
        import_string = f"""from langchain_mistralai.chat_models import ChatMistralAI"""
        code_string = f"""llm=ChatMistralAI(api_key=os.environ.get('MISTRAL_API_KEY'),model='{model}')""" 
    elif model_owner == "HF":
        logger.info(f"LLM Code Gen Invoked: {retrieval_model}")
        import_string = f"""from langchain_huggingface import HuggingFaceEndpoint"""
        code_string = f"""llm=HuggingFaceEndpoint(repo_id='{model}',huggingfacehub_api_token=os.environ.get('HUGGINGFACEHUB_API_TOKEN'))"""
    else:
        raise ValueError(f"Invalid LLM: {kwargs['retrieval_model']}")
    return {'code_string':code_string,'import_string':import_string}

 