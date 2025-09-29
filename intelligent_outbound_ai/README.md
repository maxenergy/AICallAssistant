# Intelligent Outbound AI Assistant

This project is an AI-powered outbound calling assistant that generates personalized scripts to improve communication efficiency and conversion rates.

## Project Structure

- `data/`: Stores data used for training, testing, and research.
- `docs/`: Contains project documentation.
- `intelligent_outbound_ai/`: Main application source code directory.
  - `api/`: Defines the API endpoints for interacting with the system.
  - `core/`: Includes core components like the AI model, A/B testing framework, and data models.
  - `modules/`: Contains distinct functional modules of the system.
    - `call_analyzer/`: Analyzes call transcripts and provides real-time feedback.
    - `company_research/`: Gathers and processes information about target companies.
    - `learning_system/`: Implements the continuous learning and model optimization logic.
    - `script_generator/`: Generates dynamic and personalized call scripts.
- `scripts/`: Houses utility scripts for tasks like data processing or database migration.
- `tests/`: Contains all unit, integration, and end-to-end tests.