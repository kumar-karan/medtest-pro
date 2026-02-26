# Quiz Master

Quiz Master is a "Bring Your Own Quiz" (BYOQ) web application designed to digitize and enhance the experience of taking practice exams or quizzes. It converts your own static PDF questionnaires (processed into JSON) into interactive, timed, and graded quizzes.

## Project Structure

```
/
├── index.html        # Main application entry point
├── assets/           # Static assets (PDFs, images)
├── examples/         # Example prompts and quiz files
│   ├── quiz_generation_prompt.txt
├── example_quiz.json # Sample quiz file for testing
└── README.md         # Project documentation
```

## Features

- **Bring Your Own Quiz:** Upload any quiz in JSON format.
- **Interactive Testing:** Converts static content into a dynamic quiz interface.
- **PDF Integration:** View the original PDF alongside the questions for reference (optional).
- **Auto-Fit PDF:** Automatically scales the reference PDF to fit the viewer.
- **Timer & Progress:** Track time remaining and questions completed.
- **Theme Support:** Toggle between Light and Dark modes.
- **Responsive Design:** Optimized for desktop and tablet usage.

## Setup

1.  Clone the repository.
2.  Open `index.html` in a modern web browser.
3.  **Generate Quiz JSON:**
    - Use the system prompt in `examples/quiz_generation_prompt.txt` or copy it from the app's "How to Generate Quiz JSON" modal.
    - Paste the prompt and your quiz content (text or PDF) into an AI assistant like **ChatGPT**, **Claude**, or **Gemini / AI Studio**.
    - Copy the generated JSON output.
4.  **Start Quiz:**
    - Paste the JSON into the app or upload the `.json` file.
    - (Optional) Upload the original PDF for reference.
    - Click "Start Quiz".

## Testing

For a quick test, you can upload the `example_quiz.json` file found in the root directory.

## Development

- The project uses `TailwindCSS` (via CDN) for styling.
- `PDF.js` is used for rendering PDF documents.
- No build step is required; just edit `index.html` and refresh.

## Credits

Originally developed by Karan Kumar, adapted for general use.
