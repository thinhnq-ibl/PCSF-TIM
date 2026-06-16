#!/bin/bash

# PSF-CTF Paper Build Script
# This script handles compilation with pgfplots organized in a subdirectory

cd "$(dirname "$0")" || exit

echo "🔨 Building PSF-CTF Paper..."
echo ""

# Set TEXINPUTS and BIBINPUTS to include lib subdirectory for .cls and .bst files
export TEXINPUTS=".:./lib:./pgfplots:$TEXINPUTS"
export BIBINPUTS=".:./lib:$BIBINPUTS"

# Ensure sn-basic.bst is visible to bibtex in the working directory
cp -f lib/sn-basic.bst . 2>/dev/null || true

# Compilation cycle: pdflatex -> bibtex -> pdflatex -> pdflatex
echo "📄 Pass 1: LaTeX compilation..."
pdflatex -interaction=nonstopmode draft_paper_springer.tex > /tmp/build1.log 2>&1

echo "📚 Running BibTeX..."
bibtex draft_paper_springer.aux > /tmp/bibtex.log 2>&1

echo "📄 Pass 2: LaTeX compilation..."
pdflatex -interaction=nonstopmode draft_paper_springer.tex > /tmp/build2.log 2>&1

echo "📄 Pass 3: LaTeX compilation..."
pdflatex -interaction=nonstopmode draft_paper_springer.tex > /tmp/build3.log 2>&1

echo ""
if [ -f draft_paper_springer.pdf ]; then
  SIZE=$(ls -lh draft_paper_springer.pdf | awk '{print $5}')
  echo "✅ Build successful!"
  echo "📦 Output: draft_paper_springer.pdf ($SIZE)"
  echo "📑 Pages: $(pdfinfo draft_paper_springer.pdf 2>/dev/null | grep Pages | awk '{print $2}') pages"
else
  echo "❌ Build failed! Check logs:"
  echo "  - /tmp/build1.log"
  echo "  - /tmp/bibtex.log"
  echo "  - /tmp/build2.log"
  echo "  - /tmp/build3.log"
  exit 1
fi

echo ""
echo "📁 Project structure:"
echo "  ├── draft_paper_springer.tex (main source)"
echo "  ├── draft_paper_springer.pdf (compiled output)"
echo "  ├── references.bib"
echo "  └── pgfplots/ (93 library files)"
