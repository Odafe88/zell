"""
Diagnostic script to test PDF generation speed and identify bottlenecks
"""
import time
import os
import multiprocessing
from scripts.pdf_generator import html_to_pdf
from scripts.data_loader import load_data

def test_single_pdf():
    """Test how long a single PDF takes"""
    # Find the first HTML file
    html_files = [f for f in os.listdir('reports/html') if f.endswith('.html')]
    if not html_files:
        print("No HTML files found in reports/html/")
        return
    
    test_file = html_files[0]
    report_name = test_file.replace('.html', '')
    
    print(f"Testing single PDF generation with: {test_file}")
    start = time.time()
    
    try:
        html_to_pdf(test_file, report_name)
        elapsed = time.time() - start
        print(f"✓ Single PDF generated in {elapsed:.2f} seconds")
        return elapsed
    except Exception as e:
        print(f"✗ Error: {e}")
        return None

def test_multiple_pdfs(num=5):
    """Test multiple PDFs sequentially"""
    html_files = [f for f in os.listdir('reports/html') if f.endswith('.html')][:num]
    if not html_files:
        print("No HTML files found in reports/html/")
        return
    
    print(f"\nTesting {len(html_files)} PDFs sequentially...")
    start = time.time()
    
    for html_file in html_files:
        report_name = html_file.replace('.html', '')
        try:
            html_to_pdf(html_file, report_name)
        except Exception as e:
            print(f"Error with {html_file}: {e}")
    
    elapsed = time.time() - start
    avg = elapsed / len(html_files)
    print(f"✓ {len(html_files)} PDFs generated in {elapsed:.2f} seconds")
    print(f"  Average: {avg:.2f} seconds per PDF")
    return avg

def system_info():
    """Print system information"""
    print("=" * 60)
    print("SYSTEM INFORMATION")
    print("=" * 60)
    print(f"CPU Cores: {multiprocessing.cpu_count()}")
    
    # Check if wkhtmltopdf exists
    wkhtml_path = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    if os.path.exists(wkhtml_path):
        print(f"✓ wkhtmltopdf found: {wkhtml_path}")
        # Get file size
        size = os.path.getsize(wkhtml_path) / (1024 * 1024)
        print(f"  Size: {size:.2f} MB")
    else:
        print(f"✗ wkhtmltopdf NOT found at: {wkhtml_path}")
    
    # Check data size
    try:
        data = load_data('data/raw_data.json')
        print(f"Total entries to process: {len(data)}")
    except:
        print("Could not load data file")
    
    print("=" * 60)
    print()

if __name__ == "__main__":
    system_info()
    
    single_time = test_single_pdf()
    if single_time:
        print(f"\nEstimated time for 100 PDFs: {single_time * 100 / 60:.1f} minutes (sequential)")
        print(f"Estimated time for 100 PDFs: {single_time * 100 / 6 / 60:.1f} minutes (6 processes)")
    
    test_multiple_pdfs(5)

