# FinDash-Chatbot – Intent-Aware Financial Question Answering System

FinDash is a financial intelligence API that enables users to ask **natural language questions** over structured financial data while designed to improve response reliability through controlled retrieval and validation.

The system validates user intent using financial guardrails, executes controlled database queries, and generates responses strictly from retrieved data.

## Features

* Natural language financial querying
* Intent validation and financial guardrails
* Secure SAP HANA database integration
* Structured and reliable answer generation
* Protection against hallucinated outputs
* Backend architecture designed with scalability and modularity in mind

## Tech Stack

* Python
* FastAPI
* SAP HANA
* hdbcli
* Pydantic
* python-dotenv
* OpenPyXL

## Project Workflow:

1. User submits a financial question
2. Request is validated
3. Financial guardrails are applied
4. Query is executed on SAP HANA
5. Results are processed
6. Response is generated strictly from returned data

## Project Structure

```plaintext
FinDash/
│
├── app.py
├── finance_guardrails.py
├── prompts/
├── db/
├── utils/
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd FinDash
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate environment:

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Configure environment variables:

```env
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
```

Run the application:

```bash
uvicorn main:app --reload
```

## Example Query

```text
What was the total revenue for the latest quarter?
```

Example Response:

```text
The total revenue for the latest quarter was ₹X based on available financial records.
```

## Guardrails

* No assumptions beyond available data
* No fabricated values
* No database schema exposure
* Only finance-related queries accepted

## Future Enhancements

* Multi-period analysis
* Dashboard integration
* Visualization support
* Role-based access control

## License

This project represents my independent implementation and adaptation of concepts explored during prior professional experience. The repository contains only generalized components intended for learning and portfolio purposes.

