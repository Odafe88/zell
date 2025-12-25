# Path settings for templates, input, and output
TEMPLATES_DIR = 'templates/'
OUTPUT_HTML_DIR = 'reports/html/'
OUTPUT_PDF_DIR = 'reports/pdf/'

# PDFKit options - optimized for speed
PDFKIT_OPTIONS = {
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'no-outline': None,  # Disable outline for faster generation
    'disable-javascript': None,  # Actually disable JS (empty string doesn't work!)
    'quiet': None,  # Suppress output - significantly faster
    'load-error-handling': 'ignore',  # Don't hang on missing resources
    'load-media-error-handling': 'ignore',  # Don't hang on missing images
}
