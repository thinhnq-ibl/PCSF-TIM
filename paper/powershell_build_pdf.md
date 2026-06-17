Viewed BUILD.sh:1-52

Để biên dịch file LaTeX sang định dạng PDF trên Windows, bạn có 2 cách tùy thuộc vào môi trường dòng lệnh bạn đang sử dụng:

---

### Cách 1: Sử dụng Git Bash hoặc WSL (Khuyên dùng)
Trong thư mục dự án đã có sẵn file script Bash [BUILD.sh](file:///c:/Users/Thinh%20Nguyen/OneDrive%20-%20Aarista%20Technologies/human_mobility/prepare_for_paper/paper/BUILD.sh) tự động hóa toàn bộ chu trình compile (pdflatex $\to$ bibtex $\to$ pdflatex $\to$ pdflatex) để cập nhật tài liệu tham khảo và hình ảnh:

1. Mở Git Bash (hoặc terminal WSL) và di chuyển vào thư mục chứa bài báo:
   ```bash
   cd "c:/Users/Thinh Nguyen/OneDrive - Aarista Technologies/human_mobility/prepare_for_paper/paper"
   ```
2. Cấp quyền thực thi và chạy script build:
   ```bash
   chmod +x BUILD.sh
   ./BUILD.sh
   ```

---

### Cách 2: Chạy trực tiếp từ Windows PowerShell
Nếu bạn đã cài đặt hệ thống LaTeX trên Windows (ví dụ: **TeX Live** hoặc **MiKTeX**), bạn có thể chạy tuần tự các lệnh sau trong PowerShell để biên dịch thủ công:

1. Di chuyển vào thư mục paper trong PowerShell:
   ```powershell
   cd "D:\research\PCSF-TIM\paper"
   ```

# 1. Thiết lập biến môi trường để LaTeX tìm được hình ảnh/thư viện con

```
$env:TEXINPUTS = ".;./lib;./pgfplots;$env:TEXINPUTS"
$env:BIBINPUTS = ".;./lib;$env:BIBINPUTS"
```
# 2. Thực thi chu trình biên dịch đầy đủ
```
Remove-Item -Path *.aux, *.bbl, *.blg, *.log, *.out, *.toc, *.synctex.gz, *.run.xml, *.bcf -ErrorAction SilentlyContinue
pdflatex -interaction=nonstopmode draft_paper_springer.tex
bibtex draft_paper_springer.aux
pdflatex -interaction=nonstopmode draft_paper_springer.tex
pdflatex -interaction=nonstopmode draft_paper_springer.tex
```

Sau khi hoàn thành, file PDF mới nhất sẽ được xuất ra tại thư mục hiện tại với tên: `draft_paper_springer.pdf`.