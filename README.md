# Medtest Pro

Medtest Pro is a web-based medical assessment platform designed to digitize and enhance the experience of taking medical practice exams. It converts static PDF questionnaires into interactive, timed, and graded quizzes.

## Project Structure

```
/
├── index.html        # Main application entry point
├── assets/           # Static assets (PDFs, images)
├── dev/              # Development artifacts and reference files
│   ├── ai_studio_code.*
│   ├── inspo.html
│   └── ...
└── README.md         # Project documentation
```

## Features

- **Interactive Testing:** Converts static content into a dynamic quiz interface.
- **PDF Integration:** View the original PDF alongside the questions for reference.
- **Auto-Fit PDF:** Automatically scales the reference PDF to fit the viewer.
- **Timer & Progress:** Track time remaining and questions completed.
- **Theme Support:** Toggle between Light and Dark modes.
- **Responsive Design:** Optimized for desktop and tablet usage.

## Setup

1.  Clone the repository.
2.  Open `index.html` in a modern web browser.
3.  Upload the required JSON configuration and PDF file (optional) to start an exam.

## Development

- The project uses `TailwindCSS` (via CDN) for styling.
- `PDF.js` is used for rendering PDF documents.
- No build step is required; just edit `index.html` and refresh.

## Credits

Developed by Karan Kumar.
