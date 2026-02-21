# Quiz Master

Quiz Master is a "Bring Your Own Quiz" (BYOQ) web application designed to digitize and enhance the experience of taking practice exams or quizzes. It converts your own static PDF questionnaires (processed into JSON) into interactive, timed, and graded quizzes.

## Project Structure

```
/
├── index.html        # Main application entry point
├── assets/           # Static assets (PDFs, images)
├── dev/              # Development artifacts and reference files
│   ├── quiz_generation_prompt.txt
│   └── ...
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
3.  Follow the in-app instructions to generate your quiz JSON from a PDF using AI Studio, or use an existing JSON file.
4.  Upload the JSON configuration and optional PDF file to start a quiz.

## Development

- The project uses `TailwindCSS` (via CDN) for styling.
- `PDF.js` is used for rendering PDF documents.
- No build step is required; just edit `index.html` and refresh.

## Credits

Originally developed by Karan Kumar, adapted for general use.
