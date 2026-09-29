# Hướng dẫn cài đặt và cộng tác

Dành cho Vũ Thị Phương Anh và Nguyễn Phương Linh. Kho dự án:
[eshop-clothing-next-category](https://github.com/nghonganh016/eshop-clothing-next-category).
Nhánh tích hợp: `main`. Notebook chính nằm ngay ở thư mục gốc:
`Group01_EShopClothing.ipynb`.

Kho ở chế độ riêng tư. Hồng Anh phải cấp quyền cộng tác cho tài khoản GitHub
của hai bạn; hai bạn cần chấp nhận lời mời trước khi clone hoặc push.
Không gửi mật khẩu, mã xác minh hoặc mã truy cập trong notebook, commit hay tin nhắn.

## 1. Lấy dự án lần đầu

Cài Git và Python 3.11. Mở PowerShell trên Windows hoặc Terminal trên macOS/Linux
tại thư mục cha muốn chứa dự án, rồi chạy:

```bash
git --version
git clone https://github.com/nghonganh016/eshop-clothing-next-category.git
cd eshop-clothing-next-category
git status
```

Đây là URL thật, không phải đường dẫn mẫu. Khi Git yêu cầu xác thực, đăng nhập
qua trình duyệt hoặc trình quản lý thông tin xác thực của Git. GitHub không dùng
mật khẩu tài khoản để xác thực Git qua HTTPS.

## 2. Tạo môi trường và mở notebook

Chạy từ thư mục vừa clone. Mỗi máy tự tạo `.venv` một lần, không sao chép môi
trường ảo của người khác. Các lần sau chỉ kích hoạt lại môi trường đã có.

### Windows PowerShell

```powershell
py -3.11 --version
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --user --name eshop-clothing --display-name "Python (eshop-clothing)"
python -m jupyterlab Group01_EShopClothing.ipynb
```

Nếu PowerShell chặn `Activate.ps1`, không cần đổi chính sách toàn máy. Mở
Command Prompt tại cùng thư mục và dùng môi trường đã tạo:

```bat
.venv\Scripts\activate.bat
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --user --name eshop-clothing --display-name "Python (eshop-clothing)"
python -m jupyterlab Group01_EShopClothing.ipynb
```

Cũng có thể bỏ bước kích hoạt và dùng trực tiếp
`.\.venv\Scripts\python.exe -m pip install -r requirements.txt` trong PowerShell;
các lệnh Python khác thay tiền tố `python` bằng cùng đường dẫn này.

### macOS/Linux

```bash
python3.11 --version
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m pip check
python -m ipykernel install --user --name eshop-clothing --display-name "Python (eshop-clothing)"
python -m jupyterlab Group01_EShopClothing.ipynb
```

Nếu chưa có `python3.11`, cài Python 3.11 trước; không mặc định dùng một phiên bản
bất kỳ. Một số bản Linux cần gói hỗ trợ `venv` cho Python 3.11. Nếu XGBoost trên
macOS báo thiếu `libomp`, cài OpenMP, chẳng hạn `brew install libomp` khi máy đã
có Homebrew; đây là bước xử lý lỗi theo máy, không bắt buộc chạy cho mọi người.

### Chọn nhân Python

Trong JupyterLab chọn **Kernel > Change Kernel > Python (eshop-clothing)**.
Trong VS Code, mở cả thư mục dự án, cài phần mở rộng Python và Jupyter, mở
notebook rồi chọn **Select Kernel** và môi trường `.venv` của dự án.

Kiểm tra trong Terminal đã kích hoạt môi trường:

```bash
python -c "import sys; print(sys.executable)"
python -c "import pandas, sklearn, xgboost; print(pandas.__version__, sklearn.__version__, xgboost.__version__)"
```

Đường dẫn Python phải nằm trong `.venv` của thư mục clone. Có thể chạy
`import sys; print(sys.executable)` trong một ô tạm để kiểm tra nhân notebook,
rồi xóa ô tạm trước khi commit. Khi chuyển thư mục dự án, đăng ký lại nhân.

## 3. Cấu trúc và dữ liệu

| Tệp hoặc thư mục | Vai trò |
| --- | --- |
| `Group01_EShopClothing.ipynb` | Mục 1–11 đã làm; mục 12–21 có hướng dẫn để viết tiếp |
| `e-shop clothing 2008.csv` | Dữ liệu gốc: 165.474 lượt nhấp, 14 cột; đọc bằng dấu phẩy như notebook |
| `e-shop clothing 2008 data description.txt` | Ý nghĩa, mã biến và trích dẫn nguồn; giữ nguyên bản nguồn |
| `train.csv`, `test.csv` | Bản xuất sau tạo lịch sử, nhãn và chia phiên; gồm nhãn và cột truy vết, không dùng mọi cột làm đầu vào |
| `PROJECT_CONTEXT.md` | Mục tiêu, phương pháp, mô hình và thiết kế E1–E4 |
| `TEAM_RESPONSIBILITIES.md` | Phân công thành viên |
| `TASK.md` | Tiến độ và việc chưa hoàn thành |
| `requirements.txt` | Thư viện phân tích và công cụ mở notebook |
| `tools/validate_preparation.py` | Kiểm tra cấu trúc, cú pháp và chuẩn bị dữ liệu; không sửa notebook hoặc CSV |
| `.gitignore`, `.gitattributes` | Loại tệp cục bộ và quy định cách lưu tệp bằng Git |

`references/` hiện trống nên không xuất hiện khi clone. Phương Anh có thể tạo
thư mục này để lưu danh mục tài liệu và dẫn nguồn; chỉ đưa tài liệu có quyền
chia sẻ lên kho. `.venv/`, `.eda_work/`, `.vscode/`, bộ nhớ đệm, tệp tạm và thông
tin xác thực không được đưa lên GitHub.

Giữ nguyên tên các CSV và tệp mô tả. Chạy từ thư mục gốc để đường dẫn tương đối
hoạt động. Không sửa tay `train.csv` hoặc `test.csv` để khớp một thí nghiệm.

## 4. Thứ tự chạy và điều kiện phải giữ

1. Đọc yêu cầu, phân công và hướng dẫn ngay trước ô cần làm.
2. Chọn đúng nhân, khởi động lại nhân và chạy mục 1–11 theo thứ tự. Mục 11 xuất
   lại hai CSV; nếu mã và dữ liệu không đổi thì nội dung xuất phải không đổi.
3. Kiểm tra 141.448 hàng có nhãn; 112.491 hàng/15.187 phiên huấn luyện;
   28.957 hàng/3.797 phiên kiểm tra; không có phiên trùng.
4. Phương Anh làm mục 12, thống nhất cách chuẩn bị dữ liệu và nơi lưu kết quả với
   Phương Linh, rồi làm mục 13. Phương Linh tiếp tục mục 14–18; cả nhóm viết 19–21.
5. Các ô `TODO` chỉ có chú thích và không tạo kết quả. Chạy hết notebook khi còn
   các ô này không có nghĩa dự án đã hoàn thành.

Kiểm tra dữ liệu chuẩn bị mà không thay đổi tệp:

```bash
python tools/validate_preparation.py
```

Dùng `session_split` sẵn có với `random_state=42`; không chia lại từng hàng.
Chọn đầu vào bằng danh sách đặc trưng, loại `year`, `session ID`, `next_category`.
Giá trị lịch sử bị thiếu ở lượt đầu là có chủ đích, không phải lý do xóa hàng.
Chỉ học cách điền thiếu, mã hóa và chuẩn hóa từ tập huấn luyện, bên trong từng
lần kiểm định khi chọn tham số. Kiểm định nội bộ cũng chia theo phiên; không
dùng tập kiểm tra để chọn tham số, dừng sớm hoặc chọn mô hình.

Hai nhóm đặc trưng dùng cùng mô hình, phiên kiểm tra, thước đo và quy tắc chọn
tham số. E1–E4 có lần lượt 12, 17, 20 và 23 đầu vào. Macro F1 là thước đo chính;
Accuracy và Weighted F1 bổ sung. So sánh với quy tắc “danh mục tiếp theo bằng
danh mục hiện tại”; 81,25% trong EDA là tỷ lệ toàn bộ dữ liệu có nhãn, chưa phải
kết quả quy tắc trên tập kiểm tra.

## 5. Cập nhật và tạo nhánh riêng

Không clone lại mỗi lần. Trong thư mục dự án đã có, kiểm tra rồi cập nhật:

```bash
git status
git switch main
git pull --ff-only origin main
```

Chỉ chuyển nhánh hoặc pull khi đã lưu thay đổi vào commit, hoặc chủ động cất
bằng `git stash`. Nếu Git báo thay đổi chưa lưu, xử lý trước; không dùng
`reset --hard` để bỏ cảnh báo. Khi requirements đổi, kích hoạt `.venv` và chạy
`python -m pip install -r requirements.txt`.

Phương Anh tạo nhánh lần đầu:

```bash
git switch -c codex/phuong-anh-baseline
```

Phương Linh tạo nhánh sau khi phần chuẩn bị dùng chung được gộp vào main:

```bash
git switch -c codex/phuong-linh-history
```

Đây là tên nhánh đề xuất cụ thể. Những lần sau dùng `git switch` không có `-c`.
Ví dụ cập nhật nhánh Phương Anh đã có trên GitHub:

```bash
git switch codex/phuong-anh-baseline
git pull --ff-only
git fetch origin
git merge origin/main
```

`git pull --ff-only` trên nhánh riêng chỉ dùng sau lần push đầu thiết lập nhánh
theo dõi. Phương Linh làm tương tự với `codex/phuong-linh-history`. Nếu có xung
đột, phối hợp với người phụ trách, không nhận toàn bộ notebook của một phía và
làm mất phần của bên kia; kiểm tra các ô và chạy lại trước khi commit.

## 6. Commit, push và tránh ghi đè

Hai nhánh không tự ngăn xung đột khi sửa cùng notebook. Ưu tiên bàn giao tuần tự:
Phương Anh hoàn thành mục 12 rồi mở pull request; sau khi gộp, Phương Linh cập
nhật main. Báo trong nhóm trước khi sửa notebook, phân rõ mục được sửa và không
xóa đầu ra mục 1–11 chỉ vì chạy thử trên máy mình.

Ví dụ Phương Anh lưu thay đổi đã kiểm tra:

```bash
python tools/validate_preparation.py
git status
git diff --stat
git add Group01_EShopClothing.ipynb TASK.md
git diff --cached --stat
git commit -m "Add current-feature model experiments"
git push -u origin codex/phuong-anh-baseline
```

Phương Linh dùng `git push -u origin codex/phuong-linh-history` và nội dung commit
đúng phần đã làm. `git add` ở trên chỉ đưa notebook và tiến độ vào commit; nếu
thay đổi thư viện hoặc tài liệu, đưa rõ từng tệp vào sau khi kiểm tra.

Nếu Git chưa có tác giả, thay các giá trị đánh dấu bằng thông tin của chính mình;
không chạy nguyên văn:

```bash
git config user.name "THAY_BANG_TEN_CUA_BAN"
git config user.email "THAY_BANG_EMAIL_GIT_CUA_BAN"
```

Sau khi push, mở GitHub, tạo pull request từ nhánh của mình vào `main`, nhờ một
thành viên kiểm tra trước khi gộp. Không force-push vào `main`. Lần sau trên
cùng nhánh chỉ cần `git push`. Chỉ đánh dấu hoàn thành trong `TASK.md` khi đã
chạy và có kết quả.