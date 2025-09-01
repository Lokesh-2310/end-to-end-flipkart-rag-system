# Flipkart Product Recommendation Chatbot

A sophisticated RAG (Retrieval-Augmented Generation) chatbot that provides intelligent product recommendations based on Flipkart product reviews. The system combines a FastAPI backend with a Streamlit frontend to deliver real-time product insights and recommendations.

## 🚀 Features

- **Intelligent Product Recommendations**: Uses RAG technology to provide contextual product suggestions
- **Review-Based Insights**: Leverages actual Flipkart product reviews for accurate recommendations
- **Interactive Chat Interface**: Modern Streamlit-based conversational UI
- **Vector Search**: Powered by AstraDB for efficient similarity search
- **Memory-Enabled Conversations**: Maintains chat history for contextual responses
- **Real-time API**: FastAPI backend for scalable performance

## 🏗️ Architecture

The application follows a modular architecture:

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │    FastAPI      │    │    AstraDB      │
│   Frontend      │◄──►│    Backend      │◄──►│  Vector Store   │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   Groq LLM      │
                       │ (Llama 3.1 8B)  │
                       └─────────────────┘
```

## 🛠️ Technology Stack

- **Backend**: FastAPI
- **Frontend**: Streamlit
- **LLM**: Groq (Llama 3.1 8B Instant)
- **Embeddings**: HuggingFace (BAAI/bge-base-en-v1.5)
- **Vector Database**: AstraDB
- **Framework**: LangChain
- **Data Processing**: Pandas

## 📦 Installation

### Prerequisites

- Python 3.8+
- AstraDB account and credentials
- Groq API key

### Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd end-to-end-project
   ```

2. **Create and activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**:
   Create a `.env` file in the root directory:
   ```env
   ASTRA_DB_API_ENDPOINT=your_astra_db_endpoint
   ASTRA_DB_APPLICATION_TOKEN=your_astra_db_token
   ASTRA_DB_KEYSPACE=your_keyspace_name
   GROQ_API_KEY=your_groq_api_key
   ```

## 🚀 Usage

### Data Ingestion (One-time setup)

If running for the first time, you need to ingest the product review data:

```python
from flipkart.data_ingestion import DataIngestor

# Ingest data into vector store
vector_store = DataIngestor().ingest(load_existing=False)
```

### Running the Application

1. **Start the FastAPI backend**:
   ```bash
   uvicorn main:app --reload --host 127.0.0.1 --port 8000
   ```

2. **Launch the Streamlit frontend** (in a new terminal):
   ```bash
   streamlit run frontend.py
   ```

3. **Access the application**:
   - Frontend: http://localhost:8501
   - API Documentation: http://localhost:8000/docs

### API Endpoints

#### POST `/fetch`
Processes user queries and returns AI-generated recommendations.

**Request Body**:
```json
{
  "user_input": "Recommend a good smartphone under 20000"
}
```

**Response**:
```json
{
  "messages": "Based on the reviews, I recommend the XXXXX 10 Pro..."
}
```

## 📁 Project Structure

```
end-to-end-project/
├── flipkart/
│   ├── __init__.py
│   ├── config.py           # Configuration management
│   ├── data_converter.py   # CSV to Document conversion
│   ├── data_ingestion.py   # Vector store ingestion
│   └── rag_chain.py       # RAG chain implementation
├── data/
│   └── flipkart_product_review.csv
├── main.py                # FastAPI application
├── frontend.py           # Streamlit interface
├── requirements.txt      # Dependencies
├── setup.py             # Package setup
└── README.md           # This file
```

## 🔧 Configuration

The application uses environment variables for configuration. Key settings in `flipkart/config.py`:

- **EMBEDDING_MODEL**: `BAAI/bge-base-en-v1.5`
- **RAG_MODEL**: `llama-3.1-8b-instant`
- **Collection Name**: `flipkart_recommendation_data`

## 🤖 How It Works

1. **Data Processing**: Product reviews are converted to embeddings using HuggingFace models
2. **Vector Storage**: Embeddings are stored in AstraDB for efficient retrieval
3. **Query Processing**: User queries are embedded and matched against stored reviews
4. **Context Retrieval**: Top-3 most relevant reviews are retrieved as context
5. **Response Generation**: Groq's Llama model generates responses using retrieved context
6. **Memory Management**: Chat history is maintained for contextual conversations

## 🔍 Example Queries

- "What are the best smartphones under ₹15,000?"
- "Recommend a laptop for gaming"
- "Tell me about wireless earphones with good battery life"
- "Which products have the best customer reviews?"

## 🚨 Error Handling

The application includes robust error handling:
- API connectivity issues
- Database connection failures
- Invalid user inputs
- Model inference errors

## 📈 Performance

- **Retrieval**: Top-3 similarity search with vector embeddings
- **Generation**: Llama 3.1 8B model for fast inference
- **Caching**: Vector store supports existing data loading
- **Scalability**: FastAPI backend supports concurrent requests

## 🛡️ Security

- Environment variables for sensitive credentials
- API token-based authentication for AstraDB
- Secure HTTP connections

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Lokesh** - Initial work and development

## 🙏 Acknowledgments

- Flipkart for the product review dataset
- Groq for providing fast LLM inference
- AstraDB for vector storage capabilities
- HuggingFace for embedding models
- LangChain for RAG framework

---

**Note**: Ensure you have valid API credentials for Groq and AstraDB before running the application. The system requires an active internet connection for model inference and vector storage operations.
