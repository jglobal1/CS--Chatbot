# Raw Training Data

This directory contains the raw training data for the FUT QA Assistant.

## Data Format

The training data should be in JSON format with the following structure:

```json
[
    {
        "context": "Your context text here...",
        "question": "Your question here?",
        "answers": {
            "text": ["Your answer here"],
            "answer_start": [position_in_context]
        }
    }
]
```

## Data Sources

You can prepare your training data from various sources:

1. **CSV Files**: Use `data_preparation.py` to convert CSV files
2. **Text Files**: Use `data_preparation.py` to process text and questions separately
3. **Manual Creation**: Create JSON files manually following the format above

## File Naming

- Use descriptive names like `fut_academic_data.json`
- Include version numbers if you have multiple versions
- Keep file sizes manageable (under 100MB recommended)

## Data Quality

Ensure your training data:
- Has accurate answer positions
- Covers diverse topics about FUT
- Includes various question types
- Has sufficient examples (at least 100+ recommended)
