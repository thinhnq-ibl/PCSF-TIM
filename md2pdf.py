#!/usr/bin/env python3
"""
Script chuyển đổi Markdown (.md) thành PDF với giao diện đẹp (CSS GitHub style),
hỗ trợ bảng, công thức Toán (MathJax LaTeX), highlight code block, và phân trang A4.

Sử dụng:
    python md2pdf.py input.md
    python md2pdf.py input.md -o output.pdf
"""

import sys
import os
import argparse
import subprocess
from pathlib import Path

# Đảm bảo UTF-8 output trên Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")


def install_package(package_name):
    print(f"Đang cài đặt thư viện thiếu: {package_name}...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Kiểm tra thư viện markdown
try:
    import markdown
except ImportError:
    install_package("markdown")
    import markdown

# HTML Template chuẩn đẹp cho PDF
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <!-- MathJax rendering cho LaTeX math formula -->
    <script>
    MathJax = {{
      tex: {{
        inlineMath: [['$', '$'], ['\\\\(', '\\\\)']],
        displayMath: [['$$', '$$'], ['\\\\[', '\\\\]']]
      }},
      svg: {{ fontCache: 'global' }}
    }};
    </script>
    <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>
    <style>
        @page {{
            size: A4;
            margin: 20mm 18mm 20mm 18mm;
        }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            font-size: 13.5px;
            line-height: 1.6;
            color: #24292e;
            background-color: #ffffff;
            margin: 0 auto;
            padding: 0;
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-weight: 600;
            line-height: 1.3;
            margin-top: 1.5em;
            margin-bottom: 0.6em;
            color: #1a1d20;
            page-break-after: avoid;
        }}
        h1 {{ font-size: 2.1em; border-bottom: 1.5px solid #eaecef; padding-bottom: 0.3em; margin-top: 0; }}
        h2 {{ font-size: 1.5em; border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }}
        h3 {{ font-size: 1.25em; }}
        h4 {{ font-size: 1.0em; }}
        p {{ margin-top: 0; margin-bottom: 1em; }}
        a {{ color: #0366d6; text-decoration: none; }}
        code {{
            font-family: "Cascadia Code", Consolas, Monaco, "Liberation Mono", monospace;
            font-size: 88%;
            background-color: #f3f4f6;
            padding: 0.2em 0.4em;
            border-radius: 4px;
        }}
        pre {{
            background-color: #f6f8fa;
            border: 1px solid #e1e4e8;
            border-radius: 6px;
            padding: 14px;
            overflow: auto;
            line-height: 1.45;
            page-break-inside: avoid;
            margin-bottom: 1.2em;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
            font-size: 85%;
        }}
        blockquote {{
            margin: 0 0 1.2em 0;
            padding: 0.5em 1em;
            color: #57606a;
            border-left: 0.25em solid #d0d7de;
            background-color: #f8f9fa;
        }}
        table {{
            border-spacing: 0;
            border-collapse: collapse;
            width: 100%;
            margin-top: 1em;
            margin-bottom: 1.2em;
            page-break-inside: avoid;
        }}
        table th, table td {{
            padding: 8px 12px;
            border: 1px solid #d0d7de;
        }}
        table tr:nth-child(2n) {{
            background-color: #f6f8fa;
        }}
        table th {{
            font-weight: 600;
            background-color: #f3f4f6;
            text-align: left;
        }}
        img {{
            max-width: 100%;
            height: auto;
            page-break-inside: avoid;
            display: block;
            margin: 1em auto;
        }}
        hr {{
            height: 0.15em;
            padding: 0;
            margin: 1.8em 0;
            background-color: #e1e4e8;
            border: 0;
        }}
        ul, ol {{
            padding-left: 2em;
            margin-top: 0;
            margin-bottom: 1em;
        }}
        li {{ margin-bottom: 0.3em; }}
    </style>
</head>
<body>
    {content}
</body>
</html>
"""

def md_to_html(md_path: Path) -> str:
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Convert Markdown to HTML with common extensions
    html_body = markdown.markdown(
        text,
        extensions=[
            "extra",
            "tables",
            "fenced_code",
            "codehilite",
            "toc",
            "nl2br",
            "sane_lists"
        ]
    )

    title = md_path.stem.replace("_", " ").title()
    full_html = HTML_TEMPLATE.format(title=title, content=html_body)
    return full_html

def convert_html_to_pdf_playwright(html_path: Path, pdf_path: Path):
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        install_package("playwright")
        subprocess.check_call([sys.executable, "-m", "playwright", "install", "chromium"])
        from playwright.sync_api import sync_playwright

    print(f"🔄 Đang xuất PDF thông qua Playwright Chromium...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(html_path.as_uri(), wait_until="networkidle")
        
        # Đợi MathJax load & render nếu có
        page.evaluate("() => window.MathJax ? MathJax.typesetPromise() : Promise.resolve()")
        page.wait_for_timeout(1000)

        page.pdf(
            path=str(pdf_path),
            format="A4",
            print_background=True,
            margin={"top": "20mm", "bottom": "20mm", "left": "18mm", "right": "18mm"}
        )
        browser.close()

def main():
    parser = argparse.ArgumentParser(description="Chuyển đổi file Markdown (.md) sang PDF")
    parser.add_argument("input", help="Đường dẫn file .md đầu vào")
    parser.add_argument("-o", "--output", help="Đường dẫn file .pdf đầu ra (mặc định trùng tên file md)")
    parser.add_argument("--keep-html", action="store_true", help="Giữ lại file HTML trung gian")

    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    if not input_path.exists():
        print(f"❌ Lỗi: File '{input_path}' không tồn tại!")
        sys.exit(1)

    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = input_path.with_suffix(".pdf")

    temp_html_path = input_path.with_suffix(".temp.html")

    print(f"📄 Đang đọc file Markdown: {input_path.name}")
    html_content = md_to_html(input_path)

    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    try:
        convert_html_to_pdf_playwright(temp_html_path, output_path)
        print(f"✅ Đã chuyển đổi thành công sang PDF: {output_path}")
    except Exception as e:
        print(f"❌ Có lỗi khi tạo PDF: {e}")
    finally:
        if not args.keep_html and temp_html_path.exists():
            temp_html_path.unlink()

if __name__ == "__main__":
    main()
